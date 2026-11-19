# 🟡 挖空练习 6：战绩 JSON 存盘（学习 with open + json.dump）
# 目标：写出 1 个把牌局数据保存到 JSON 文件的函数（约 6~7 行）

import json
import os


def save_game(filepath, players, scores, history):
    """把玩家列表、当前分数和历史记录保存到指定的 JSON 文件。

    功能要求：
    1. 把 players、scores、history 打包放进一个字典 data 里：
       data = {
           "players": players,
           "scores": scores,
           "history": history,
       }
    2. 用 with open(filepath, "w", encoding="utf-8") as f: 打开文件（"w" 表示写入）
    3. 调用 json.dump(data, f, ensure_ascii=False, indent=2) 把字典存进文件
       （ensure_ascii=False 让中文不乱码，indent=2 让格式整齐）
    """
    # TODO: 请在这里补全代码（约 6~7 行）
    data = {
           "players": players,
           "scores": scores,
           "history": history,
       }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# --- 下方是配套读档函数与测试外壳，不用修改 ---
def load_game(filepath):
    """如果存档存在就读取并返回字典，否则返回 None。"""
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    test_file = os.path.join(os.path.dirname(__file__), "test_save.json")
    test_players = ["张三", "李四", "王五"]
    test_scores = {"张三": 3, "李四": 0, "王五": 2}
    test_history = [
        {"winners": ["张三"], "points": 1},
        {"winners": ["张三", "王五"], "points": 2},
    ]

    save_game(test_file, test_players, test_scores, test_history)
    loaded = load_game(test_file)
    print("读回来的存档内容：", loaded)

    assert loaded is not None, "没有读到存档文件，检查 save_game 是否正确写入！"
    assert loaded["players"] == test_players
    assert loaded["scores"] == test_scores
    assert loaded["history"] == test_history
    os.remove(test_file)  # 测完顺手删掉临时测试文件
    print("✅ 测试通过！JSON 存盘功能已搞定！")
