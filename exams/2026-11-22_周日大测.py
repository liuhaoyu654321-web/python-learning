"""
====================================================================
2026-11-22 周日大测（第 1 章 1.4~1.8 综合摸底）
定位与难度：综合覆盖 02打牌记分器 / 03歌词记忆助手 / 04决策转盘 核心基本功｜难度：适中（偏基础巩固）
满分：100 分｜建议时长：40~50 分钟

作答纪律：
1. 闭卷独立完成，不翻看旧项目代码或笔记；
2. 第 1 题请在 `# 作答(1)：` / `# 作答(2)：` 后用大白话写出原因和改法；
3. 第 2 题请直接修改函数里的 Bug；
4. 第 3~6 题请在函数体 `# TODO:` 下方补全代码（可以删掉 `pass`）；
5. 做完后告诉 AI“交卷”，即可自动运行校验并批改记分；
6. 若实在卡住，可喊“给个 1 级提示”（将按规酌情扣分，保证成绩真实）。
====================================================================
"""

import json


# ====================================================================
# 第 1 题（12 分｜读代码找错｜考察点：1.4 range 包头不包尾、1.6 return 位置）
# 请阅读下面两段有问题的代码（均为注释），分别回答：
# 哪里错了？运行会出现什么现象？应该怎么改？
# ====================================================================

# (1)（6 分）想按 "1号" 到 "n号" 依次让 n 位玩家输入名字（例如 n = 3 时输入 1号、2号、3号）
# players = []
# for i in range(1, n):
#     name = input(f"请输入 {i} 号玩家名字: ").strip()
#     players.append(name)
#
# 作答(1)：range(1, n)这里，括号里的n应该加一才对。如果不加n，它会少算一位，相当于是1~n-1。少算一位玩家。应该把括号里的n加一才对。


# (2)（6 分）想把列表 raw_list 里所有非空字符串收集到 result 里并返回
# def clean_list(raw_list):
#     result = []
#     for s in raw_list:
#         if s.strip():
#             result.append(s.strip())
#         return result
#
# 作答(2)：Return应该和for对齐，它这里没有对齐，如果只是放在这里，循环第一次，for循环就会停止。直接return


# ====================================================================
# 第 2 题（13 分｜改 Bug 实战｜考察点：1.8 排错、1.4 0 起始下标、1.6 方法括号）
# 场景：用户按屏幕上看到的 1 号、2 号、3 号编号选歌，返回对应歌名；
#       如果输入的不是有效编号，则返回 None。
# 下面函数里埋了 2 个 Bug，请直接修改函数代码使其通过全部样例。
#
# 输入输出样例：
# - fix_pick_song(["稻香", "晴天", "七里香"], " 1 ")  -> "稻香"
# - fix_pick_song(["稻香", "晴天", "七里香"], "3")    -> "七里香"
# - fix_pick_song(["稻香", "晴天", "七里香"], "0")    -> None
# - fix_pick_song(["稻香", "晴天", "七里香"], "abc")  -> None
# ====================================================================
def fix_pick_song(titles, user_input):
    raw = user_input.strip()
    if raw.isdigit() and 1 <= int(raw) <= len(titles):
        return titles[int(raw) - 1]
    return None


# ====================================================================
# 第 3 题（15 分｜核心函数手写｜考察点：1.4 range 与列表相邻下标）
# 要求：传入歌词列表 lines，返回所有相邻上下句拼成的列表，
#       每项格式为 f"{上一句} -> {下一句}"；
#       如果歌词少于 2 句，返回空列表 []。
#
# 输入输出样例：
# - make_pairs(["A", "B", "C", "D"]) -> ["A -> B", "B -> C", "C -> D"]
# - make_pairs(["只有一句"])          -> []
# - make_pairs([])                   -> []
# ====================================================================
def make_pairs(lines):
    # TODO:
    # todos = list[range(lines.split())]
    # for idx, todo in todos:
    result = []
    for i in range(len(lines) - 1):
        result.append(f"{lines[i]} -> {lines[i+1]}")
    return result    
  

    


# ====================================================================
# 第 4 题（18 分｜核心函数手写｜考察点：1.5 字典存取与分类统计）
# 要求：传入每局赢家名字列表 winners，返回一个字典，记录每人赢了多少局；
#       若传入空列表 []，返回 {}。
#
# 输入输出样例：
# - count_wins(["小明", "小红", "小明", "阿强", "小明"]) -> {"小明": 3, "小红": 1, "阿强": 1}
# - count_wins([]) -> {}
# ====================================================================
def count_wins(winners):
    # TODO:
    #for name in winners:
       # count_wins += Winners[]
    status = {}
    for name in winners:
        status[name] = status.get(name,0) + 1
    return status       



# ====================================================================
# 第 5 题（18 分｜核心函数手写｜考察点：1.8 条件筛选与列表/字典遍历）
# 要求：传入菜品列表 items（每项如 {"name": "黄焖鸡", "price": 25}）和最高预算 max_price。
#       - 若 max_price <= 0，表示不限预算，返回所有菜品的 name 列表；
#       - 否则只保留 price <= max_price 的菜品，返回符合条件的 name 列表。
#
# 输入输出样例：
# items = [
#     {"name": "黄焖鸡", "price": 25},
#     {"name": "烤鱼", "price": 68},
#     {"name": "拌面", "price": 18},
# ]
# - filter_affordable(items, 30) -> ["黄焖鸡", "拌面"]
# - filter_affordable(items, 0)  -> ["黄焖鸡", "烤鱼", "拌面"]
# - filter_affordable(items, 10) -> []
# ====================================================================
def filter_affordable(items, max_price):
    # TODO:
    #for item in items:
        #if max_price <= 0 :
            #return items[name]
       #item[price] <= max_price    
    result = []
    for item in items:
        if max_price <= 0 or item["price"] <= max_price:
            result.append(item["name"])
    return result           



# ====================================================================
# 第 6 题（24 分｜实用场景综合题｜考察点：1.6 文本清洗、1.5 字典更新、1.7 JSON 永久读写）
# 要求：编写函数 save_clean_note(filepath, notes, title, raw_text)：
#   1. 把多行字符串 raw_text 按行拆开（可用 .splitlines()），去掉每行前后空格，
#      丢弃空行，得到干净的列表 lines；
#   2. 把 title 作为键、lines 作为值存入字典 notes；
#   3. 用 with open(..., "w", encoding="utf-8") 和
#      json.dump(..., ensure_ascii=False, indent=2) 把更新后的 notes 写入 filepath；
#   4. 返回清洗后的列表 lines。
#
# 输入输出样例：
# - 输入 notes = {}，title = "买菜清单"，raw_text = "  鸡蛋 \n\n  西红柿  \n   \n葱"
# - 返回值：["鸡蛋", "西红柿", "葱"]
# - 此时 notes 变为 {"买菜清单": ["鸡蛋", "西红柿", "葱"]}，且 filepath 中已保存对应 JSON 内容。
# ====================================================================
def save_clean_note(filepath, notes, title, raw_text):
    # TODO:
    #ines = raw_text.splitlines()
    #notes = title[lines]
    #with open(filepath,"w",encoding="utf-8") as f:
        #son.dump(filepath, f,ensure_ascii=False, indent=2)
    #return lines    
    lines = []
    for s in raw_text.splitlines():
        if s.strip():
            lines.append(s.strip())
    notes[title] = lines
    with open(filepath, "w",encoding="utf-8") as f:
        json.dump(notes,f,ensure_ascii=False, indent=2)    
    return lines        

        

