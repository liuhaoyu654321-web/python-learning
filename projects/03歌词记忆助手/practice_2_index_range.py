# 🟡 挖空练习 2：第 1.4 节专项——循环与下标定位（[i - 1] 选歌 + 相邻两句歌词配对）
# 【看懂优先级】🔴 现在要看懂并亲手写（核心基本功）｜🟡 看大意就行｜🟢 现在完全不用管（自动测试外壳）
# 目标：独立完成下面 2 个小函数（合计约 12~14 行），彻底拿下第 1.4 节！


# 🔴 练习 A（约 4~5 行）：按屏幕编号（从 1 开始）取出对应歌名
def pick_song_by_num(titles, raw_num):
    """根据用户输入的编号字符串 raw_num，从歌名列表 titles 中取出对应歌名。

    功能要求：
    1. 去掉 raw_num 首尾空格（可用 .strip()）
    2. 判断它是不是纯数字，并且转成整数后在 1 到 列表长度 之间
    3. 如果合法，返回对应位置的歌名（注意：屏幕编号从 1 开始，列表下标从 0 开始！）
    4. 如果不合法（比如 "0"、"99"、"abc"、""），返回 None

    输入样例与期望输出：
    - pick_song_by_num(["晴天", "七里香", "送别"], "1")   -> "晴天"
    - pick_song_by_num(["晴天", "七里香", "送别"], " 3 ") -> "送别"
    - pick_song_by_num(["晴天", "七里香", "送别"], "0")   -> None
    - pick_song_by_num(["晴天", "七里香", "送别"], "4")   -> None
    - pick_song_by_num(["晴天", "七里香", "送别"], "abc") -> None
    """
    # TODO: 请在这里补全代码（约 4~5 行，写完删掉下面的 pass）
    num = raw_num.strip()
    if  num.isdigit() and  1 <= int(num) <= len(titles):
        return titles[int(num) -1]
    return None    

 


# 🔴 练习 B（约 8~10 行）：清洗歌词列表，并用下标把“上一句 → 下一句”配成题库
def build_lyric_pairs(raw_lines):
    """把原始歌词列表 raw_lines 清洗后，按相邻顺序配成「上一句 → 下一句」题库列表。

    功能要求：
    1. 注意输入类型：raw_lines 已经是一个列表（list），里面每个元素是一行文字。
    2. 先建一个空列表 lines，遍历 raw_lines，去掉空行和首尾空格，把有效歌词放进 lines。
    3. 再建一个空列表 pairs，用下标循环依次取出“当前句”和“下一句”（注意别越界！）：
       每一对做成字典 {"prompt": 当前句, "answer": 下一句}，追加到 pairs。
    4. 返回 pairs（如果有效歌词少于 2 句，自然返回空列表 []）。

    输入样例与期望输出：
    - raw_lines = ["  长亭外，古道边 ", "", "   ", "芳草碧连天  ", "晚风拂柳笛声残"]
    - 清洗后 lines = ["长亭外，古道边", "芳草碧连天", "晚风拂柳笛声残"]
    - 期望返回：
      [
          {"prompt": "长亭外，古道边", "answer": "芳草碧连天"},
          {"prompt": "芳草碧连天", "answer": "晚风拂柳笛声残"},
      ]
    """
    # TODO: 请在这里补全代码（约 8~10 行，写完删掉下面的 pass）
    lines = []
    for line in raw_lines:
        s = line.strip()
        if s:
          lines.append(s)
    pairs = []
    for i in range(len(lines) - 1 ):
        pairs.append({"prompt":lines[i],"answer":lines[i+1]})
    return pairs


# --- 下方是自动测试外壳，不用修改 ---

# 🟢 不用管：运行本文件会自动检查你写的两个函数对不对
if __name__ == "__main__":
    print("=== 测试练习 A：pick_song_by_num ===")
    demo_titles = ["晴天", "七里香", "送别"]
    assert pick_song_by_num(demo_titles, "1") == "晴天", "编号 1 应该拿到第 0 项 '晴天'！"
    assert pick_song_by_num(demo_titles, " 3 ") == "送别", "编号 3（含空格）应该拿到 '送别'！"
    assert pick_song_by_num(demo_titles, "0") is None, "编号 0 超出范围，应返回 None！"
    assert pick_song_by_num(demo_titles, "4") is None, "编号 4 超出范围，应返回 None！"
    assert pick_song_by_num(demo_titles, "abc") is None, "非数字输入应返回 None！"
    print("[通过] 练习 A（编号与 0 起始下标）全部正确！")

    print("\n=== 测试练习 B：build_lyric_pairs ===")
    demo_raw = ["  长亭外，古道边 ", "", "   ", "芳草碧连天  ", "晚风拂柳笛声残"]
    expected = [
        {"prompt": "长亭外，古道边", "answer": "芳草碧连天"},
        {"prompt": "芳草碧连天", "answer": "晚风拂柳笛声残"},
    ]
    res = build_lyric_pairs(demo_raw)
    print("你的输出：", res)
    assert res == expected, f"结果不对哦！期望：{expected}，实际：{res}"
    assert build_lyric_pairs(["只有一句歌词"]) == [], "只有 1 句歌词时配不成对，应返回 []！"
    assert build_lyric_pairs([]) == [], "空列表应返回 []！"
    print("[通过] 练习 B（列表遍历与相邻下标 range）全部正确！")
    print("\n🎉 恭喜！第 1.4 节专项挖空全部通关！")
