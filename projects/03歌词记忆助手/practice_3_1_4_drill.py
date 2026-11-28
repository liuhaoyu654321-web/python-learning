# 🟡 挖空练习 3：第 1.4 节错题强化 4 连刷（肌肉记忆专练）
# 【看懂优先级】🔴 现在要看懂并亲手写（核心基本功）｜🟡 看大意就行｜🟢 现在完全不用管（自动测试外壳）
# 专治刚才 4 个错点：
#   1) 编号转数字是 int(num) 不是 len(num)，合法判断别乱加 not
#   2) 取/删列表项用 列表名[下标] / 列表名.pop(下标)，不是 list(...)
#   3) range() 里必须传数字 len(...)，相邻对比要 - 1
#   4) 遍历列表不用 .split()，去空行记得 if s:
# 目标：尽量 0 提示独立跑通全部 4 题，跑通即直接通关第 1.4 节！


# 🔴 题 1（约 5 行）：按屏幕编号（从 1 开始）删除并返回那一项
def delete_item_by_num(items, raw_num):
    """根据输入的编号字符串 raw_num，从列表 items 中删除对应项并返回它。

    功能要求：
    1. 去掉 raw_num 首尾空格
    2. 判断它是纯数字，且转成整数后在 1 到 items 长度之间
    3. 合法则用 .pop(...) 弹出对应 0 起始下标的元素并返回
    4. 不合法（"0"、"99"、"abc"、""）返回 None，且不要修改 items

    输入样例：
    - items = ["拉面", "盖饭", "饺子"]
    - delete_item_by_num(items, " 2 ") -> 返回 "盖饭"，此时 items 变成 ["拉面", "饺子"]
    - delete_item_by_num(items, "0")   -> 返回 None，items 不变
    """
    # TODO: 请在这里补全代码（约 5 行，写完删掉下面的 pass）
    num = raw_num.strip()
    if num.isdigit() and 1 <= int(num) <= len(items):
        return items.pop(int(num) -1)
    return None    


# 🔴 题 2（约 5 行）：用 range + 下标，把名单转成带 1 起始编号的列表
def format_menu_lines(names):
    """给名单列表 names 加上从 1 开始的编号，返回新的字符串列表。

    功能要求：
    1. 创建空列表 result
    2. 用 for i in range(...): 遍历每个下标（注意 range 括号里放数字！）
    3. 把 f"{i + 1}. {names[i]}" 追加到 result
    4. 返回 result

    输入样例：
    - format_menu_lines(["小明", "小红", "小刚"]) -> ["1. 小明", "2. 小红", "3. 小刚"]
    - format_menu_lines([]) -> []
    """
    # TODO: 请在这里补全代码（约 5 行，写完删掉下面的 pass）
    pass


# 🔴 题 3（约 5 行）：计算相邻两天的花销差值（后一天 - 前一天）
def calc_daily_diffs(costs):
    """给定每天花销列表 costs，返回每一天相比前一天的花销变化列表。

    功能要求：
    1. 创建空列表 diffs
    2. 用下标循环遍历到倒数第二天（别越界！），把「后一天减前一天」的结果放进 diffs
    3. 返回 diffs（少于 2 天返回 []）

    输入样例：
    - calc_daily_diffs([20, 35, 30, 50]) -> [15, -5, 20]
    - calc_daily_diffs([10]) -> []
    - calc_daily_diffs([]) -> []
    """
    # TODO: 请在这里补全代码（约 5 行，写完删掉下面的 pass）
    pass


# 🔴 题 4（约 8~9 行）：综合题——清洗列表空项 + 找出连续两天重复吃的店名
def find_repeated_neighbors(raw_records):
    """把原始记录列表 raw_records 去空清洗后，找出相邻重复出现的店名列表。

    功能要求：
    1. 注意：raw_records 已经是列表（list），不是一整段字符串！
    2. 先建空列表 clean，遍历 raw_records，去掉首尾空格后过滤掉空项，放进 clean
    3. 再建空列表 repeated，用下标循环比较相邻两项：如果当前项和下一项相同，就把当前项加进 repeated
    4. 返回 repeated

    输入样例：
    - raw_records = [" 拉面 ", "", "拉面", "  ", "盖饭", "饺子", "饺子"]
    - 清洗后 clean = ["拉面", "拉面", "盖饭", "饺子", "饺子"]
    - 期望返回：["拉面", "饺子"]
    """
    # TODO: 请在这里补全代码（约 8~9 行，写完删掉下面的 pass）
    pass


# --- 下方是自动测试外壳，不用修改 ---

# 🟢 不用管：运行本文件会自动检查 4 道题是否全部通过
if __name__ == "__main__":
    print("=== 测试题 1：delete_item_by_num ===")
    foods = ["拉面", "盖饭", "饺子"]
    assert delete_item_by_num(foods, " 2 ") == "盖饭", "编号 2 应删掉并返回 '盖饭'！"
    assert foods == ["拉面", "饺子"], f"删除后原列表不对，实际：{foods}"
    assert delete_item_by_num(foods, "0") is None and foods == ["拉面", "饺子"], "编号 0 应返回 None 且不改列表！"
    assert delete_item_by_num(foods, "5") is None and foods == ["拉面", "饺子"], "越界编号应返回 None！"
    assert delete_item_by_num(foods, "abc") is None, "非数字应返回 None！"
    print("[通过] 题 1 全部正确！")

    print("\n=== 测试题 2：format_menu_lines ===")
    assert format_menu_lines(["小明", "小红", "小刚"]) == ["1. 小明", "2. 小红", "3. 小刚"], "编号格式不对！"
    assert format_menu_lines([]) == [], "空列表应返回 []！"
    print("[通过] 题 2 全部正确！")

    print("\n=== 测试题 3：calc_daily_diffs ===")
    assert calc_daily_diffs([20, 35, 30, 50]) == [15, -5, 20], "差值计算不对！"
    assert calc_daily_diffs([10]) == [], "只有 1 天应返回 []！"
    assert calc_daily_diffs([]) == [], "空列表应返回 []！"
    print("[通过] 题 3 全部正确！")

    print("\n=== 测试题 4：find_repeated_neighbors ===")
    sample = [" 拉面 ", "", "拉面", "  ", "盖饭", "饺子", "饺子"]
    res4 = find_repeated_neighbors(sample)
    print("题 4 输出：", res4)
    assert res4 == ["拉面", "饺子"], f"期望 ['拉面', '饺子']，实际：{res4}"
    assert find_repeated_neighbors(["只有一家"]) == [], "只有 1 条记录应返回 []！"
    assert find_repeated_neighbors(["", "   "]) == [], "全空记录应返回 []！"
    print("[通过] 题 4 全部正确！")

    print("\n🎉 太强了！第 1.4 节错题强化 4 连刷全部通关！")
