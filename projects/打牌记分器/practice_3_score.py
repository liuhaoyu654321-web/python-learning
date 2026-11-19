# 🟡 挖空练习 3：按编号给赢家加分（对应 card_score.py 第 29~35 行）
# 目标：独立写出 1 个根据编号字符串给赢家加分的函数（约 6~7 行）


def add_scores(players, scores, choice):
    """根据用户输入的赢家编号字符串，给对应玩家 +1 分，并返回本局赢家名字列表。

    功能要求：
    1. 创建一个空列表 winners，用来存本局加分的人名
    2. 用 choice.split() 按空格拆开，遍历每一小段 part
    3. 如果 part 是纯数字，且转成 int 后在 1 到 len(players) 之间：
       - 用列表下标取出玩家名字（注意：屏幕 1 号对应列表第 0 个，要 - 1）
       - 在 scores 字典里给这位玩家 +1 分
       - 把这位玩家名字加进 winners 列表
    4. 循环结束后返回 winners

    输入样例与期望行为：
    - players = ["张三", "李四", "王五"]
    - scores = {"张三": 0, "李四": 0, "王五": 0}
    - choice = "1 3 99 abc"
    - 返回 winners = ["张三", "王五"]，同时 scores 变成 {"张三": 1, "李四": 0, "王五": 1}
    """
    # TODO: 请在这里补全代码（约 6~7 行）
    winners = []
    for part in choice.split():
       if part.isdigit() and 1 <= int(part) <= len(players):
           winner = players[int(part)- 1]
           scores[winner] += 1
           winners.append(winner)
    return winners



# --- 下方是测试外壳，不用修改 ---
if __name__ == "__main__":
    test_players = ["张三", "李四", "王五"]
    test_scores = {"张三": 0, "李四": 0, "王五": 0}
    result = add_scores(test_players, test_scores, "1 3 99 abc")
    print(f"本局赢家 = {result}")
    print(f"最新分数 = {test_scores}")
    assert result == ["张三", "王五"], f"期望赢家是 ['张三', '王五']，实际拿到 {result}"
    assert test_scores == {"张三": 1, "李四": 0, "王五": 1}, f"分数不对哦：{test_scores}"
    print("✅ 测试通过！1号和3号成功加分，99和abc被正确忽略了！")
