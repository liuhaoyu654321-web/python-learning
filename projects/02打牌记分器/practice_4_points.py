# 🟡 挖空练习 4：自定义本局加分（巩固输入校验 + or 默认值 + return）
# 目标：不看旧代码提示，独立写出 1 个获取本局分值的函数（约 5~6 行）


def get_round_points():
    """获取本局每人加多少分（1~100 的整数，直接回车默认返回 1）。

    功能要求：
    1. 反复提示用户输入："请输入本局加几分（1~100，直接回车默认 1 分）: "
    2. 去掉首尾空格后，如果用户直接回车，默认当成 "1"
    3. 如果输入是纯数字，且转成整数后在 1 到 100 之间，就返回这个整数（int）
    4. 否则打印提示："请输入 1~100 之间的数字。" 然后继续让用户重输

    输入样例与期望行为：
    - 直接回车        -> 返回整数 1
    - 输入 "abc"      -> 打印提示，继续让用户重输
    - 输入 "0" / "150"-> 打印提示，继续让用户重输
    - 输入 "5"        -> 返回整数 5
    """
    # TODO: 请在这里补全代码（约 5~6 行）
    while True:
        raw = input("请输入本局加几分(1 ~ 100,直接回车默认1分) :") .strip() or "1"
        if raw.isdigit() and 1 <= int(raw) <= 100:
            return int(raw)
        else:
            print("请输入 1~100 之间的数字。")    

    


# --- 下方是配套加分函数与测试外壳，不用修改 ---
def add_scores(players, scores, choice, points):
    """按编号给本局赢家加上指定分值 points。"""
    winners = []
    for part in choice.split():
        if part.isdigit() and 1 <= int(part) <= len(players):
            winner = players[int(part) - 1]
            scores[winner] += points
            winners.append(winner)
    return winners


if __name__ == "__main__":
    points = get_round_points()
    print(f"\n设置成功！本局加分 = {points} 分，数据类型 = {type(points)}")
    assert type(points) is int and 1 <= points <= 100, "返回值必须是 1~100 的整数哦！"

    test_players = ["张三", "李四", "王五"]
    test_scores = {"张三": 0, "李四": 0, "王五": 0}
    winners = add_scores(test_players, test_scores, "1 3", points)
    print(f"模拟本局 {winners} 赢牌，最新分数 = {test_scores}")
    assert test_scores == {"张三": points, "李四": 0, "王五": points}
    print("✅ 测试通过！建议多跑两次，测测：直接回车、输字母、输 0、输 5。")
