# 歌词记忆助手 V1（极简初版：选歌 -> 接下一句 -> 错句自动重练）
SONGS = {
    "周杰伦 - 晴天": """（把《晴天》歌词粘贴替换这里，每句一行）""",
    "周杰伦 - 夜曲": """（把《夜曲》歌词粘贴替换这里，每句一行）""",
    "周杰伦 - 星晴": """（把《星晴》歌词粘贴替换这里，每句一行）""",
    "试玩：送别（中文）": """
长亭外，古道边
芳草碧连天
晚风拂柳笛声残
夕阳山外山""",
    "试玩：Twinkle Star（英文）": """
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.""",
}

titles = list(SONGS.keys())
print("=== 歌词记忆助手 ===")
for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")
while True:
    raw = input(f"请选歌 (1~{len(titles)}，回车默认 4 先试玩): ").strip() or "4"
    if raw.isdigit() and 1 <= int(raw) <= len(titles):
        title = titles[int(raw) - 1]
        break
    print("请输入有效编号。")

lines = []
for s in SONGS[title].splitlines():
    if s.strip():
        lines.append(s.strip())
if len(lines) < 2:
    print(f"《{title}》还没贴歌词！打开文件粘进三引号里再运行即可。")
    raise SystemExit

todo = list(range(len(lines) - 1))
round_num = 1
while todo:
    print(f"\n--- 第 {round_num} 轮（剩余 {len(todo)} 句）《{title}》 ---")
    wrong = []
    for idx in todo:
        print(f"\n上一句：{lines[idx]}")
        input("想好下一句后按回车看答案...")
        print(f"下一句：{lines[idx + 1]}")
        if input("记住了吗？(回车=记住 / n=没记住): ").strip().lower() == "n":
            wrong.append(idx)
    todo = wrong
    round_num += 1
print(f"\n恭喜！《{title}》全曲接词通关！")
