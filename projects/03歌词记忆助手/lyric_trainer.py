# 歌词记忆助手（极简瘦身版：选歌、接下一句、错句自动重练、添加新歌存 JSON）
# 【看懂优先级】🔴 现在要看懂（核心基本功）｜🟡 看大意就行（先不抠细节）｜🟢 现在完全不用管（工具套话/进阶语法，直接跳过）

# 🟢 不用管：固定工具配置（导入 JSON 和文件路径模块，指定曲库文件）
import json
import os
SONGS_FILE = os.path.join(os.path.dirname(__file__), "songs.json")

# 🔴 现在要看懂：新歌清洗、加入字典并保存 JSON（你亲手写过的核心函数）
def add_and_save_song(filepath, songs, title, raw_lyrics):
    lines = []
    for s in raw_lyrics.splitlines():
        if s.strip():
            lines.append(s.strip())
    songs[title] = lines
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(songs, f, ensure_ascii=False, indent=2)
    return lines

# 🟡 看大意就行：读取 JSON 曲库，没有文件就返回空字典 {}（os.path.exists 🟢 不用背）
def load_songs(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# 🔴 现在要看懂：单首歌曲练习（range 生成题号 + while todo 错句自动重练）
def practice_song(title, lines):
    todo = list(range(len(lines) - 1))
    round_num = 1
    while todo:
        print(f"\n--- 第 {round_num} 轮（剩余 {len(todo)} 句）《{title}》 ---")
        wrong = []
        for idx in todo:
            print(f"\n上一句：{lines[idx]}")  # 🔴 下标定位：idx 是当前句，idx + 1 是下一句
            input("想好下一句后按回车看答案...")
            print(f"下一句：{lines[idx + 1]}")
            if input("记住了吗？(回车=记住 / n=没记住): ").strip().lower() == "n":  # 🟡 .lower() 转小写
                wrong.append(idx)
        todo = wrong
        round_num += 1
    print(f"\n恭喜！《{title}》全曲接词通关！")

# 🔴 现在要看懂：主菜单循环（选歌编号 / a 添加新歌 / q 退出）
def main():
    songs = load_songs(SONGS_FILE)
    while True:
        titles = list(songs.keys())
        print("\n=== 歌词记忆助手 ===")
        # 🟢 不用背 enumerate：把歌名从 1 开始编号打印出来
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title}（{len(songs[title])}句）")
        raw = input("输入编号选歌（a 添加新歌，q 退出）: ").strip()
        if raw.lower() == "q":
            break
        if raw.lower() == "a":
            title = input("新歌名（回车取消）: ").strip()
            if not title:
                continue
            print("请粘贴歌词（最后单独一行输入 end 结束）：")
            raw_lines = []
            while True:
                line = input()
                if line.strip().lower() == "end":
                    break
                raw_lines.append(line)
            if not raw_lines:
                continue
            lines = add_and_save_song(SONGS_FILE, songs, title, "\n".join(raw_lines))  # 🟢 '\n'.join 不用背
            print(f"已保存《{title}》，共 {len(lines)} 句！")
            continue
        if raw.isdigit() and 1 <= int(raw) <= len(titles):
            title = titles[int(raw) - 1]  # 🔴 列表 0 起始下标：屏幕 1 号对应第 0 项
            practice_song(title, songs[title])
        else:
            print("请输入有效编号，或输入 a / q。")

# 🟢 完全不用管：Python 固定启动开关，跳过就行
if __name__ == "__main__":
    main()
