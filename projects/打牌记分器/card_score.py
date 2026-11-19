# 打牌记分器（支持自定义人数、每把自定义加分、撤回、JSON 自动存盘与读档）

import json
import os

SAVE_FILE = os.path.join(os.path.dirname(__file__), "save_data.json")


def get_round_points():
    """获取本局每人加多少分（1~100 的整数，直接回车默认返回 1）。"""
    while True:
        raw = input("请输入本局加几分（1~100，直接回车默认 1 分）: ").strip() or "1"
        if raw.isdigit() and 1 <= int(raw) <= 100:
            return int(raw)
        print("请输入 1~100 之间的数字。")


def undo_last_round(scores, history):
    """撤回上一把的加分记录。"""
    if not history:
        print("还没有可撤回的记录。")
        return False
    last = history.pop()
    for name in last["winners"]:
        scores[name] -= last["points"]
    print(f"已撤回上一把：{', '.join(last['winners'])} 各 -{last['points']} 分")
    return True


def save_game(filepath, players, scores, history):
    """把玩家列表、当前分数和历史记录保存到指定的 JSON 文件。"""
    data = {
        "players": players,
        "scores": scores,
        "history": history,
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_game(filepath):
    """如果存档存在就读取并返回字典，否则返回 None。"""
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def init_game():
    """初始化牌局：有存档时询问是否继续，否则新建牌局。"""
    saved = load_game(SAVE_FILE)
    if saved is not None:
        ans = input("检测到上次存档，是否继续？(y/n，直接回车默认继续): ").strip().lower() or "y"
        if ans == "y":
            players = saved["players"]
            scores = saved["scores"]
            history = saved["history"]
            print(f"已读取存档，共 {len(history)} 把记录！")
            return players, scores, history

    while True:
        raw = input("请输入玩家人数（1~10，直接回车默认 6 人）: ").strip() or "6"
        if raw.isdigit() and 1 <= int(raw) <= 10:  # 因为 input() 拿到的永远是文字（比如 "6"），必须用 int("6") 转成整数 6
            num_players = int(raw)
            break
        print("请输入 1~10 之间的数字。")

    players = []
    print(f"请输入 {num_players} 位玩家名字（直接回车则用默认名字）：")
    for i in range(1, num_players + 1):  # （数字范围生成器）：生成从 1 到 num_players 的连续整数。
        name = input(f"玩家 {i}: ").strip() or f"玩家{i}"
        players.append(name)

    # 用字典（dictionary）记录每个人的总分，初始都是 0 分
    scores = {name: 0 for name in players}
    return players, scores, []


def main():
    players, scores, history = init_game()
    round_num = len(history) + 1

    while True:
        print(f"\n--- 第 {round_num} 把 ---")
        for idx, name in enumerate(players, 1):  # 普通 for 循环只能拿到名字 name，套上 enumerate(..., 1) 就能同时拿到“从 1 开始的序号 idx”和“名字 name”。
            print(f"{idx}. {name} ({scores[name]}分)")

        choice = input("输入本局赢家编号（多人用空格隔开，u 撤回上一把，q 结束）: ").strip()
        if choice.lower() == "q":
            break
        if choice.lower() == "u":
            if undo_last_round(scores, history):
                round_num = max(1, round_num - 1)
                save_game(SAVE_FILE, players, scores, history)
            continue

        winners = []
        for part in choice.split():
            if part.isdigit() and 1 <= int(part) <= len(players):
                winner = players[int(part) - 1]  # Python 列表的 index（索引/位置编号）是从 0 开始数的。你屏幕上看到的 1号玩家，在列表里其实是第 0 个位置，所以必须 - 1 才找对人
                winners.append(winner)

        if winners:
            points = get_round_points()
            for winner in winners:
                scores[winner] += points
            history.append({"winners": winners, "points": points})
            save_game(SAVE_FILE, players, scores, history)
            print(f"本局加分：{', '.join(winners)} 各 +{points} 分")
            round_num += 1
        else:
            print(f"输入无效，请输入 1~{len(players)} 的编号，或 u / q。")

    print("\n=== 最终得分榜 ===")
    for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score} 分")


if __name__ == "__main__":
    main()
