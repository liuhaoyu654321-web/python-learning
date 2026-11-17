# 打牌记分器（最多支持10人）

while True:
    raw = input("请输入玩家人数（1~10，直接回车默认 6 人）: ").strip() or "6"
    if raw.isdigit() and 1 <= int(raw) <= 10:
        num_players = int(raw)
        break
    print("请输入 1~10 之间的数字。")

players = []
print(f"请输入 {num_players} 位玩家名字（直接回车则用默认名字）：")
for i in range(1, num_players + 1):
    name = input(f"玩家 {i}: ").strip() or f"玩家{i}"
    players.append(name)

# 用字典（dictionary）记录每个人的总分，初始都是 0 分
scores = {name: 0 for name in players}
round_num = 1

while True:
    print(f"\n--- 第 {round_num} 把 ---")
    for idx, name in enumerate(players, 1):
        print(f"{idx}. {name} ({scores[name]}分)")

    choice = input("输入本局赢家编号（多人用空格隔开，输入 q 结束）: ").strip()
    if choice.lower() == "q":
        break

    winners = []
    for part in choice.split():
        if part.isdigit() and 1 <= int(part) <= len(players):
            winner = players[int(part) - 1]
            scores[winner] += 1
            winners.append(winner)

    if winners:
        print(f"本局加分：{', '.join(winners)} 各 +1 分")
        round_num += 1
    else:
        print(f"输入无效，请输入 1~{len(players)} 的编号。")

print("\n=== 最终得分榜 ===")
for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {score} 分")
