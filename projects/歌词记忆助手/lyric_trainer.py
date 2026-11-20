# 歌词记忆助手（支持选歌、接下一句、错句自动重练、终端添加新歌并自动保存到 JSON）
# 【看懂优先级】🔴 现在要看懂（核心基本功）｜🟡 看大意就行（先不抠细节）｜🟢 现在完全不用管（工具套话/进阶语法，直接跳过）

# 🟢 不用管：固定工具配置（导入 JSON 和文件路径模块，指定曲库存档位置）
import json
import os

SONGS_FILE = os.path.join(os.path.dirname(__file__), "songs.json")

# 🟡 看大意就行：内置初始曲库（首次运行时会自动清洗并同步存进 songs.json）
SONGS = {
    "周杰伦 - 等你下课": """
你住的巷子裡 我租了一間公寓
為了想與你不期而遇
高中三年我為什麼
為什麼不好好讀書
沒考上跟你一樣的大學

我找了份工作
離你宿舍很近
當我開始學會做蛋餅
才發現你不吃早餐
喔你又擦肩而過
你耳機聽什麼
能不能告訴我

躺在你學校的操場看星空
教室裡的燈還亮著你沒走
記得我寫給你的情書
都什麼年代了到現在我還在寫著
總有一天總有一年會發現
有人默默的陪在你的身邊
也許我不該在你的世界
當你收到情書也代表我已經走遠

學校旁的廣場
我在這等鐘聲響
等你下課一起走好嗎
談著琴唱你愛的歌
暗戀一點都不痛苦
痛苦的是你根本沒看我
我唱這麼走心
卻走不進你心裏
在人來人往找尋著你
守護著你不求結局
喔你又擦肩而過
我唱告白氣球
終於你回了頭

躺在你學校的操場看星空
教室裡的燈還亮著你沒走
記得我寫給你的情書
都什麼年代了
到現在我還在寫著
總有一天總有一年會發現
有人默默的陪在你的身邊
也許我不該在你的世界
當你收到情書也代表我已經走遠

""",
}

# 🔴 现在要看懂：新歌清洗、加入字典并保存 JSON（你刚在 practice_1 写好的核心函数）
def add_and_save_song(filepath, songs, title, raw_lyrics):
    lines = []
    for s in raw_lyrics.splitlines():
        if s.strip():
            lines.append(s.strip())
    songs[title] = lines
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(songs, f, ensure_ascii=False, indent=2)
    return lines


# 🟡 看大意就行：如果 JSON 曲库存在就读回来，不存在返回 None（os.path.exists 🟢 不用背）
def load_songs(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# 🟡 看大意就行：启动时读出 songs.json；内置 SONGS 里有还没录入的歌就自动存进去
def init_songs():
    songs = load_songs(SONGS_FILE) or {}
    for title, raw_lyrics in SONGS.items():
        if title not in songs:
            valid = 0
            for s in raw_lyrics.splitlines():
                if s.strip():
                    valid += 1
            if valid >= 2:
                add_and_save_song(SONGS_FILE, songs, title, raw_lyrics)
    return songs


# 🟡 看大意就行：在终端粘贴添加一首新歌（允许中间有空行，单独输入 end 结束）
def input_new_song(songs):
    title = input("请输入新歌名（直接回车取消）: ").strip()
    if not title:
        print("已取消添加。")
        return
    print("请粘贴歌词（可直接粘贴多行，含空行也没关系；最后单独一行输入 end 回车结束）：")
    raw_lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        raw_lines.append(line)
    valid = 0
    for s in raw_lines:
        if s.strip():
            valid += 1
    if valid < 2:
        print("有效歌词不足 2 句，已取消保存。")
        return
    raw_lyrics = "\n".join(raw_lines)  # 🟢 '\n'.join(...) 把多行列表拼回整段文字，不用背
    lines = add_and_save_song(SONGS_FILE, songs, title, raw_lyrics)
    print(f"已保存《{title}》，共 {len(lines)} 句歌词！")


# 🔴 现在要看懂：单首歌曲练习（range 生成题号 + while todo 错句自动重练）
def practice_song(title, lines):
    todo = list(range(len(lines) - 1))
    round_num = 1
    while todo:
        print(f"\n--- 第 {round_num} 轮（剩余 {len(todo)} 句）《{title}》 ---")
        wrong = []
        for idx in todo:
            print(f"\n上一句：{lines[idx]}")  # 🔴 看懂下标：idx 是上一句，下一行的 idx + 1 是紧挨着的下一句
            input("想好下一句后按回车看答案...")
            print(f"下一句：{lines[idx + 1]}")
            if input("记住了吗？(回车=记住 / n=没记住): ").strip().lower() == "n":  # 🟡 .lower() 转小写，大 N 小 n 都能认
                wrong.append(idx)
        todo = wrong
        round_num += 1
    print(f"\n恭喜！《{title}》全曲接词通关！")


# 🔴 现在要看懂：主菜单循环（编号选歌 + 输入 a 添加新歌 + 输入 q 退出）
def main():
    songs = init_songs()
    while True:
        titles = list(songs.keys())
        print("\n=== 歌词记忆助手 ===")
        if titles:
            # 🟢 不用背 enumerate：知道它负责把歌名从 1 开始编号打印出来就行
            for i, title in enumerate(titles, 1):
                print(f"{i}. {title}（{len(songs[title])}句）")
            raw = input(f"请选歌 (1~{len(titles)}，回车默认 1；a 添加新歌，q 退出): ").strip() or "1"
        else:
            raw = input("曲库还是空的，输入 a 添加新歌，或 q 退出: ").strip()

        if raw.lower() == "q":
            print("拜拜，下次继续背歌词！")
            break
        if raw.lower() == "a":
            input_new_song(songs)
            continue
        if raw.isdigit() and 1 <= int(raw) <= len(titles):
            title = titles[int(raw) - 1]  # 🔴 列表 0 起始下标：屏幕 1 号对应第 0 项
            practice_song(title, songs[title])
        else:
            print("请输入有效编号，或输入 a / q。")


# 🟢 完全不用管：Python 固定启动开关，跳过就行
if __name__ == "__main__":
    main()
