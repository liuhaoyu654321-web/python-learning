# 🟡 挖空练习 2：收集玩家名字（对应 card_score.py 第 10~14 行）
# 目标：独立写出 1 个收集玩家名字列表的函数（约 5~6 行）


def get_players(num_players):
    """根据玩家人数，收集每位玩家的名字并返回列表。

    功能要求：
    1. 创建一个空列表 players
    2. 循环从 1 到 num_players（注意 range 包头不包尾，末尾要 + 1）
    3. 每次提示：input(f"玩家 {i}: ")，去掉首尾空格后，如果直接回车就默认用 f"玩家{i}"
    4. 把拿到的名字放进 players 列表里
    5. 循环结束后返回 players 列表

    输入样例与期望行为（假设 num_players = 3）：
    - 依次输入 "张三"、直接回车、"李四"
    - 返回列表：["张三", "玩家2", "李四"]
    """
    # TODO: 请在这里补全代码（约 5~6 行）
    players = []
    for i in range( 1,num_players + 1):
        name = input(f"玩家 {i}: ").strip() or f"玩家{i}"
        players.append(name)
    return players
     



# --- 下方是测试外壳，不用修改 ---
if __name__ == "__main__":
    result = get_players(3)
    print(f"\n收集结果 = {result}，人数 = {len(result)}")
    assert isinstance(result, list) and len(result) == 3, "返回值必须是包含 3 个名字的列表哦！"
    print("✅ 测试通过！建议试试：有人输名字、有人直接回车，看看默认名字对不对。")
