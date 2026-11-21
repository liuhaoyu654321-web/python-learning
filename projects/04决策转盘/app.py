# 🟢 外壳引擎：完全不用看！只需运行本文件启动网页，日常只看和改 logic.py
# 【看懂优先级】🔴 现在要看懂（核心基本功）｜🟡 看大意就行（先不抠细节）｜🟢 现在完全不用管（外壳套话，跳过）

import argparse
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib
import json
import os
import sys
import threading
import traceback
from urllib.parse import parse_qs, urlparse
import webbrowser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")
HTML_FILE = os.path.join(BASE_DIR, "index.html")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

LOCK = threading.Lock()


def get_logic():
    """Reload logic.py on every call so edits take effect without restarting."""
    importlib.invalidate_caches()
    if "logic" in sys.modules:
        return importlib.reload(sys.modules["logic"])
    return importlib.import_module("logic")


def format_logic_error(exc):
    """Extract clean file/line info so the browser bug-radar card can highlight it."""
    if isinstance(exc, SyntaxError):
        lineno = exc.lineno or "?"
        code_line = (exc.text or "").strip()
        msg = exc.msg or str(exc)
    else:
        frames = traceback.extract_tb(exc.__traceback__)
        target = None
        for frame in frames:
            if frame.filename.endswith("logic.py"):
                target = frame
        if target is None and frames:
            target = frames[-1]
        lineno = target.lineno if target else "?"
        code_line = (target.line or "").strip() if target else ""
        msg = str(exc)
    return {
        "type": type(exc).__name__,
        "line": lineno,
        "code": code_line,
        "message": msg,
        "traceback": traceback.format_exc(),
    }


def parse_tags(raw_tags):
    if isinstance(raw_tags, list):
        return [str(t).strip() for t in raw_tags if str(t).strip()]
    if isinstance(raw_tags, str):
        normalized = raw_tags.replace("，", ",").replace(" ", ",")
        return [t.strip() for t in normalized.split(",") if t.strip()]
    return []


def collect_all_tags(items):
    seen = set()
    ordered = []
    for item in items:
        for tag in item.get("tags", []):
            if tag not in seen:
                seen.add(tag)
                ordered.append(tag)
    return ordered


def build_state(lg, data, max_price=0, exclude_tags=None):
    items = data.setdefault("items", [])
    history = data.setdefault("history", [])
    candidates = lg.filter_items(items, max_price, exclude_tags or [])
    stats = lg.count_by_category(history)
    return {
        "ok": True,
        "items": items,
        "candidates": candidates,
        "history": history,
        "stats": stats,
        "all_tags": collect_all_tags(items),
    }


def find_winner_index(candidates, winner):
    for i, item in enumerate(candidates):
        if item.get("name") == winner.get("name") and item.get("price") == winner.get("price"):
            return i
    return 0


class ReusableThreadingHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = True


class WheelHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Keep terminal quiet except startup banner and errors.
        pass

    def _send_bytes(self, status, content_type, payload_bytes):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload_bytes)))
        self.end_headers()
        self.wfile.write(payload_bytes)

    def _send_json(self, status, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self._send_bytes(status, "application/json; charset=utf-8", body)

    def _read_json_body(self):
        length = int(self.headers.get("Content-Length", "0") or 0)
        if length <= 0:
            return {}
        raw = self.rfile.read(length).decode("utf-8")
        return json.loads(raw) if raw.strip() else {}

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ("/", "/index.html"):
            try:
                with open(HTML_FILE, "rb") as f:
                    self._send_bytes(200, "text/html; charset=utf-8", f.read())
            except OSError as exc:
                self._send_json(500, {"ok": False, "error": format_logic_error(exc)})
            return

        if parsed.path == "/api/state":
            qs = parse_qs(parsed.query)
            try:
                max_price = int((qs.get("max_price") or ["0"])[0] or 0)
            except ValueError:
                max_price = 0
            raw_tags = (qs.get("exclude_tags") or [""])[0]
            exclude_tags = [t.strip() for t in raw_tags.split(",") if t.strip()]
            with LOCK:
                try:
                    lg = get_logic()
                    data = lg.load_data(DATA_FILE)
                    self._send_json(200, build_state(lg, data, max_price, exclude_tags))
                except Exception as exc:
                    self._send_json(500, {"ok": False, "error": format_logic_error(exc)})
            return

        self._send_json(404, {"ok": False, "error": {"type": "NotFound", "line": "-", "code": "", "message": "接口不存在"}})

    def do_POST(self):
        parsed = urlparse(self.path)
        try:
            body = self._read_json_body()
        except Exception as exc:
            self._send_json(400, {"ok": False, "error": format_logic_error(exc)})
            return

        try:
            max_price = int(body.get("max_price", 0) or 0)
        except (TypeError, ValueError):
            max_price = 0
        exclude_tags = parse_tags(body.get("exclude_tags", []))

        with LOCK:
            try:
                lg = get_logic()
                data = lg.load_data(DATA_FILE)

                if parsed.path == "/api/spin":
                    candidates = lg.filter_items(data.setdefault("items", []), max_price, exclude_tags)
                    winner = lg.pick_winner(candidates)
                    if winner is None:
                        state = build_state(lg, data, max_price, exclude_tags)
                        state["winner"] = None
                        state["winner_index"] = -1
                        self._send_json(200, state)
                        return

                    winner_index = find_winner_index(candidates, winner)
                    data.setdefault("history", []).append({
                        "name": winner["name"],
                        "category": winner["category"],
                        "price": winner["price"],
                        "time": datetime.now().strftime("%H:%M:%S"),
                    })
                    lg.save_data(DATA_FILE, data)
                    state = build_state(lg, data, max_price, exclude_tags)
                    state["winner"] = winner
                    state["winner_index"] = winner_index
                    self._send_json(200, state)
                    return

                if parsed.path == "/api/add":
                    name = str(body.get("name", "")).strip()
                    if not name:
                        self._send_json(400, {
                            "ok": False,
                            "error": {
                                "type": "输入提示",
                                "line": "-",
                                "code": "",
                                "message": "选项名称不能为空！",
                                "traceback": "",
                            },
                        })
                        return
                    category = str(body.get("category", "")).strip() or "其他"
                    try:
                        price = max(0, int(body.get("price", 0) or 0))
                    except (TypeError, ValueError):
                        price = 0
                    tags = parse_tags(body.get("tags", []))
                    data.setdefault("items", []).append({
                        "name": name,
                        "category": category,
                        "price": price,
                        "tags": tags,
                    })
                    lg.save_data(DATA_FILE, data)
                    self._send_json(200, build_state(lg, data, max_price, exclude_tags))
                    return

                if parsed.path == "/api/delete":
                    try:
                        number = int(body.get("number", 0))
                    except (TypeError, ValueError):
                        number = 0
                    removed = lg.delete_item(data.setdefault("items", []), number)
                    if removed is not None:
                        lg.save_data(DATA_FILE, data)
                    state = build_state(lg, data, max_price, exclude_tags)
                    state["removed"] = removed
                    self._send_json(200, state)
                    return

                if parsed.path == "/api/clear_history":
                    data["history"] = []
                    lg.save_data(DATA_FILE, data)
                    self._send_json(200, build_state(lg, data, max_price, exclude_tags))
                    return

                self._send_json(404, {"ok": False, "error": {"type": "NotFound", "line": "-", "code": "", "message": "接口不存在"}})
            except Exception as exc:
                self._send_json(500, {"ok": False, "error": format_logic_error(exc)})


def start_server(preferred_port):
    """Try preferred_port first, falling back if Windows reserves or occupies it."""
    candidates = [0] if preferred_port == 0 else list(dict.fromkeys([preferred_port, 18766, 18767, 18888, 0]))
    last_err = None
    for port in candidates:
        try:
            return ReusableThreadingHTTPServer(("127.0.0.1", port), WheelHandler)
        except OSError as exc:
            last_err = exc
    raise last_err


def main():
    parser = argparse.ArgumentParser(description="炫酷决策转盘本地服务")
    parser.add_argument("--port", type=int, default=18765, help="监听端口（默认 18765）")
    parser.add_argument("--no-browser", action="store_true", help="启动后不自动打开浏览器")
    args = parser.parse_args()

    server = start_server(args.port)
    actual_port = server.server_address[1]
    url = f"http://127.0.0.1:{actual_port}"
    print("==========================================")
    print(f"🎰 炫酷决策转盘已启动：{url}")
    print("⚡ 热更新开启：改完 logic.py 按 Ctrl+S，直接点网页按钮即生效！")
    print("按 Ctrl+C 可随时停止服务。")
    print("==========================================")
    sys.stdout.flush()

    if not args.no_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 服务已停止。")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
