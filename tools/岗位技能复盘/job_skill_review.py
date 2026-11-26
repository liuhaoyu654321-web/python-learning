#!/usr/bin/env python3
"""岗位技能复盘：每 3 天读取 JobFinder 数据库（只读），统计反复出现的技能，供 AI 校准学习路线。

用法（用 JobFinder 自带的 Python 运行）：
  job_skill_review.py gate [--force]   → 输出 DUE 或 SKIP <原因>
  job_skill_review.py report           → 统计 + 存快照 + 打印新增正文
  job_skill_review.py done             → 分析完成后更新 state.json

判定“确实多次出现”的规则（与定时任务提示词一致）：
  - 达标：A+B 正文命中 ≥ MIN_JDS 条，且来自 ≥ MIN_COMPANIES 家不同公司
  - 确认：本期和上一期快照都达标（confirmed=True）才允许新增技能行
  - 档位调整：占比相对上一期变化 ≥ SHIFT_PP 个百分点，且上一期变化方向相同
"""
import argparse
import importlib.util
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE_PATH = HERE / "state.json"
SNAP_DIR = HERE / "snapshots"
JOBFINDER = Path.home() / "Library/Application Support/JobFinder"
DIGEST_PATH = JOBFINDER / "jobfinder/skill_digest.py"
RULES_PATH = JOBFINDER / "jobfinder/rules.json"
DB_PATH = JOBFINDER / "岗位榜单/jobs.db"

INTERVAL_DAYS = 3
MIN_JDS = 5
MIN_COMPANIES = 3
SHIFT_PP = 5.0
MAX_JD_PRINT = 40
JD_CHARS = 800


def load_digest():
    """按路径导入 JobFinder 的 skill_digest.py，复用它的技能表和工具函数。"""
    spec = importlib.util.spec_from_file_location("skill_digest", DIGEST_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_state():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {}


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def connect():
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def today_local(dg):
    return datetime.now(dg.TZ).date()


def latest_run(conn):
    row = conn.execute("SELECT id, run_at FROM runs ORDER BY id DESC LIMIT 1").fetchone()
    return (row[0], row[1]) if row else (0, "")


def cmd_gate(args):
    if not DB_PATH.exists() or not DIGEST_PATH.exists():
        print("SKIP 本机没有 JobFinder 数据库（可能是另一台电脑）")
        return
    dg = load_digest()
    state = load_state()
    today = today_local(dg)
    last = state.get("last_review_date")
    if not last:
        last = dg.load_watermark().get("last_date")
    conn = connect()
    run_id, run_at = latest_run(conn)
    conn.close()
    if args.force:
        print(f"DUE (force) 上次分析={last} 最新抓取={run_at}")
        return
    if last:
        days = (today - date.fromisoformat(last)).days
        if days < INTERVAL_DAYS:
            print(f"SKIP 距上次分析 {days} 天（{last}），满 {INTERVAL_DAYS} 天才分析")
            return
    if run_id <= int(state.get("last_run_id", 0)):
        print(f"SKIP 上次分析后还没有新的抓取记录（最新 run #{run_id} {run_at}）")
        return
    print(f"DUE 上次分析={last} 最新抓取=#{run_id} {run_at}")


def previous_snapshot(today_str):
    if not SNAP_DIR.exists():
        return None
    files = sorted(p for p in SNAP_DIR.glob("*.json") if p.stem < today_str)
    return json.loads(files[-1].read_text(encoding="utf-8")) if files else None


def meets(jds, companies):
    return jds >= MIN_JDS and companies >= MIN_COMPANIES


def cmd_report(args):
    dg = load_digest()
    today = today_local(dg)
    today_str = today.isoformat()
    state = load_state()
    since = state.get("last_review_date") or dg.load_watermark().get("last_date") or today_str

    rules_version = json.loads(RULES_PATH.read_text(encoding="utf-8"))["version"]
    conn = connect()
    run_id, run_at = latest_run(conn)
    rows = conn.execute("""
        SELECT j.uid, j.source, j.title, j.company, j.city, j.salary, j.tags,
               j.jd_text, j.first_seen, j.updated_at, e.category, e.score
        FROM jobs j
        LEFT JOIN evaluations e ON j.uid = e.uid AND e.rules_version = ?
        ORDER BY COALESCE(e.score, 0) DESC, j.uid
    """, (rules_version,)).fetchall()
    conn.close()

    ab = [r for r in rows if r[10] in ("A", "B")]
    ab_jd = [r for r in ab if r[7] and len(str(r[7]).strip()) > 60]
    n_jd = len(ab_jd)
    text_of = lambda r: f"{r[2] or ''} {r[6] or ''} {r[7] or ''}"
    company_of = lambda r: (r[3] or "").strip() or r[0]

    prev = previous_snapshot(today_str)
    prev_skills = (prev or {}).get("skills", {})
    prev_terms = (prev or {}).get("emerging", {})

    compiled, known_tokens = dg.compile_curated()
    skills = {}
    for group, name, rxs in compiled:
        hits = [r for r in ab_jd if dg.matches_any(text_of(r), rxs)]
        jds, comps = len(hits), len({company_of(r) for r in hits})
        share = round(100.0 * jds / n_jd, 1) if n_jd else 0.0
        p = prev_skills.get(name, {})
        delta = round(share - p["share"], 1) if "share" in p else None
        prev_delta = p.get("delta")
        shift = (
            delta is not None and prev_delta is not None and abs(delta) >= SHIFT_PP
            and (delta > 0) == (prev_delta > 0) and abs(prev_delta) > 0
        )
        ok = meets(jds, comps)
        skills[name] = {
            "group": group, "jds": jds, "companies": comps, "share": share, "delta": delta,
            "meets": ok, "confirmed": ok and bool(p.get("meets")), "shift_confirmed": shift,
        }

    # 新兴词：不在策展技能表里、反复出现的英文/混合技术词
    curated_rxs = [rx for _, _, rxs in compiled for rx in rxs]
    term_jds, term_comps = Counter(), defaultdict(set)
    for r in ab_jd:
        for tok in set(re.findall(r"\b[A-Za-z][A-Za-z0-9.+#/-]{1,23}\b", text_of(r))):
            low = tok.lower().strip(".-+/")
            if len(low) < 2 or low in dg.STOPWORDS or low in known_tokens:
                continue
            if any(rx.search(tok) for rx in curated_rxs):
                continue
            term_jds[low] += 1
            term_comps[low].add(company_of(r))
    emerging = {}
    for term, jds in term_jds.most_common():
        comps = len(term_comps[term])
        if jds < 2:
            break
        ok = meets(jds, comps)
        emerging[term] = {
            "jds": jds, "companies": comps, "meets": ok,
            "confirmed": ok and bool(prev_terms.get(term, {}).get("meets")),
        }

    snapshot = {
        "date": today_str, "run_id": run_id, "run_at": run_at, "rules_version": rules_version,
        "counts": {"total": len(rows), "ab": len(ab), "ab_jds": n_jd,
                   "ab_jds_zhilian": sum(1 for r in ab_jd if r[1] == "zhilian"),
                   "ab_jds_boss": sum(1 for r in ab_jd if r[1] == "boss"),
                   "c": sum(1 for r in rows if r[10] == "C"),
                   "d": sum(1 for r in rows if r[10] == "D")},
        "thresholds": {"min_jds": MIN_JDS, "min_companies": MIN_COMPANIES, "shift_pp": SHIFT_PP},
        "skills": skills, "emerging": emerging,
    }
    SNAP_DIR.mkdir(exist_ok=True)
    (SNAP_DIR / f"{today_str}.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    c = snapshot["counts"]
    print(f"TODAY: {today_str} | SINCE: {since} | PREV_SNAPSHOT: {(prev or {}).get('date', 'none')}")
    print(f"LATEST_RUN: #{run_id} {run_at} | rules={rules_version}")
    print(f"COUNTS: total={c['total']} | A+B={c['ab']} | A+B正文={n_jd} (智联 {c['ab_jds_zhilian']} / BOSS {c['ab_jds_boss']}) | C={c['c']} | D={c['d']}")
    print(f"规则: 达标=正文≥{MIN_JDS}条且≥{MIN_COMPANIES}家公司；confirmed=连续两期达标；shift=占比变化≥{SHIFT_PP}pp且连续两期同向")

    print("\n=== 策展技能（A+B 正文）===")
    print("分组 | 技能 | 正文数 | 公司数 | 占比% | 较上期pp | 达标 | 确认 | 档位变化确认")
    for name, s in sorted(skills.items(), key=lambda kv: -kv[1]["jds"]):
        if not s["jds"]:
            continue
        d = "—" if s["delta"] is None else f"{s['delta']:+.1f}"
        print(f"{s['group']} | {name} | {s['jds']} | {s['companies']} | {s['share']} | {d} | "
              f"{'Y' if s['meets'] else '-'} | {'Y' if s['confirmed'] else '-'} | {'Y' if s['shift_confirmed'] else '-'}")

    print("\n=== 新兴词（不在技能表中，正文≥2）===")
    shown = list(emerging.items())[:40]
    for term, e in shown:
        tag = "确认" if e["confirmed"] else ("达标(待下期确认)" if e["meets"] else "观察")
        print(f"  {term}: 正文 {e['jds']} / 公司 {e['companies']} → {tag}")
    if not shown:
        print("  (none)")

    new_jd = [r for r in ab_jd if dg.to_local_date(r[8]) >= since or dg.to_local_date(r[9]) >= since]
    print(f"\n=== {since} 以来新增/更新的 A+B 正文：{len(new_jd)} 条（显示前 {min(len(new_jd), MAX_JD_PRINT)} 条）===")
    for i, r in enumerate(new_jd[:MAX_JD_PRINT], 1):
        jd = re.sub(r"\s+", " ", str(r[7])).strip()[:JD_CHARS]
        print(f"[{i}] ({r[1]} | {r[10]}/{(r[11] or 0):.0f} | {r[4]} | {r[5]}) {r[2]} @ {r[3]}")
        print(f"    JD: {jd}")


def cmd_done(args):
    dg = load_digest()
    snap = SNAP_DIR / f"{today_local(dg).isoformat()}.json"
    if not snap.exists():
        sys.exit("还没有今天的快照，先运行 report")
    s = json.loads(snap.read_text(encoding="utf-8"))
    save_state({"last_review_date": s["date"], "last_run_id": s["run_id"], "last_run_at": s["run_at"],
                "counts": s["counts"]})
    print(f"已记录：last_review_date={s['date']} last_run_id={s['run_id']}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("gate")
    g.add_argument("--force", action="store_true")
    sub.add_parser("report")
    sub.add_parser("done")
    args = ap.parse_args()
    {"gate": cmd_gate, "report": cmd_report, "done": cmd_done}[args.cmd](args)


if __name__ == "__main__":
    main()
