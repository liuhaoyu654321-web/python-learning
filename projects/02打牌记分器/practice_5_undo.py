# 🟡 挖空练习 5：撤回上一把（学习 list.pop() + 字典减分）
# 目标：写出 1 个撤回上一把加分记录的函数（约 7~8 行）


def undo_last_round(scores, history):
    """撤回上一把的加分记录。

    数据格式说明：
    - scores 是当前总分字典，例如：{"张三": 3, "李四": 0, "王五": 3}
    - history 是历史记录列表，每把存一个字典，例如：
      [
          {"winners": ["张三"], "points": 1},
          {"winners": ["张三", "王五"], "points": 2},
      ]

    功能要求：
    1. 如果 history 是空的（没有可撤回的记录）：
       - 打印 "还没有可撤回的记录。"
       - 返回 False
    2. 否则，用 history.pop() 取出并删掉最后一条记录，存到变量 last 里
    3. 遍历 last["winners"] 里的每位玩家 name：
       - 在 scores 字典里把这位玩家的分数减去 last["points"]
    4. 打印提示：f"已撤回上一把：{', '.join(last['winners'])} 各 -{last['points']} 分"
    5. 返回 True

    期望行为：
    - 撤回第 2 把（张三、王五各 2 分）后，scores 变回 {"张三": 1, "李四": 0, "王五": 1}
    - history 长度减 1，返回 True
    - 连续撤回直到 history 为空时，再调用会打印提示并返回 False
    """
    # TODO: 请在这里补全代码（约 7~8 行）
    if  not history:
        print("还没有可撤回的记录。")
        return False
    else:
        last = history.pop()
        for name in last["winners"]:
            scores[name] -= last["points"]
        print(f"已撤回上一把：{', '.join(last['winners'])}各 -{last['points']} 分")
        return True



# --- 下方是测试外壳，不用修改 ---
if __name__ == "__main__":
    test_scores = {"张三": 3, "李四": 0, "王五": 2}
    test_history = [
        {"winners": ["张三"], "points": 1},
        {"winners": ["张三", "王五"], "points": 2},
    ]

    print("撤回前：", test_scores)
    ok1 = undo_last_round(test_scores, test_history)
    print("第 1 次撤回后：", test_scores)
    assert ok1 is True
    assert test_scores == {"张三": 1, "李四": 0, "王五": 0}, f"分数不对：{test_scores}"
    assert len(test_history) == 1

    ok2 = undo_last_round(test_scores, test_history)
    print("第 2 次撤回后：", test_scores)
    assert ok2 is True
    assert test_scores == {"张三": 0, "李四": 0, "王五": 0}
    assert len(test_history) == 0

    ok3 = undo_last_round(test_scores, test_history)
    assert ok3 is False, "history 为空时应该返回 False 哦！"
    print("✅ 测试通过！撤回功能已搞定！")
