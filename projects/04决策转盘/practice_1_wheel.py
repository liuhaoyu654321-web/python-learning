# 决策转盘 - 挖空热身练习 1（三段式筛选 + 字典统计与 JSON 存盘）
# 【看懂优先级】🔴 现在要看懂（核心基本功）｜🟡 看大意就行（先不抠细节）｜🟢 现在完全不用管（工具套话，跳过）

import json
import os


# 🔴 现在要看懂：第 1 关（约 5~6 行）
# 任务：从菜品列表 items 里，找出所有价格 <= max_price 的菜名，装进一个新列表返回。
# 输入样例：
#   items = [
#       {"name": "黄焖鸡米饭", "category": "中餐", "price": 24},
#       {"name": "轻食沙拉", "category": "轻食", "price": 28},
#       {"name": "兰州拉面", "category": "面食", "price": 18},
#   ]
#   max_price = 25
# 期望输出：["黄焖鸡米饭", "兰州拉面"]
def get_affordable_names(items, max_price):
    # TODO: 在这里写你的代码（记得三段式：建空容器 -> 循环加工 -> 循环外 return）
    names = []
    for item in items :
        if item["price"] <= max_price :
            names.append(item["name"])
    return names        


# 🔴 现在要看懂：第 2 关（约 7~8 行）
# 任务：
#   1. 遍历历史记录 history，统计每个分类（"category"）各抽中过几次，存成字典 stats。
#   2. 把统计结果字典 stats 用 UTF-8 编码、缩进 2 格存到 filepath 对应的 JSON 文件里。
#   3. 返回统计字典 stats。
# 输入样例：
#   history = [
#       {"name": "黄焖鸡米饭", "category": "中餐", "price": 24},
#       {"name": "兰州拉面", "category": "面食", "price": 18},
#       {"name": "隆江猪脚饭", "category": "中餐", "price": 22},
#   ]
#   filepath = "test_stats.json"
# 期望输出：{"中餐": 2, "面食": 1}（同时生成内容相同的 test_stats.json 文件）
def save_category_stats(history, filepath):
    # TODO: 在这里写你的代码
    status = {}
    for s in history:
        cat = s["category"]
        status[cat] =status.get(cat,0)+1
    with open(filepath,"w",encoding= "utf-8") as f:
        json.dump(status,f,ensure_ascii = False,indent= 2)
    return status     
    
     



# 🟢 现在完全不用管：下面这段是自动验收代码，写完直接运行本文件就能看结果
if __name__ == "__main__":
    sample_items = [
        {"name": "黄焖鸡米饭", "category": "中餐", "price": 24},
        {"name": "轻食沙拉", "category": "轻食", "price": 28},
        {"name": "兰州拉面", "category": "面食", "price": 18},
    ]
    sample_history = [
        {"name": "黄焖鸡米饭", "category": "中餐", "price": 24},
        {"name": "兰州拉面", "category": "面食", "price": 18},
        {"name": "隆江猪脚饭", "category": "中餐", "price": 22},
    ]

    # 验收第 1 关
    res1 = get_affordable_names(sample_items, 25)
    print("第 1 关返回：", res1)
    assert res1 == ["黄焖鸡米饭", "兰州拉面"], f"第 1 关期望 ['黄焖鸡米饭', '兰州拉面']，实际得到 {res1}"
    print("✅ 第 1 关通过！\n")

    # 验收第 2 关
    test_file = os.path.join(os.path.dirname(__file__), "test_stats.json")
    if os.path.exists(test_file):
        os.remove(test_file)

    res2 = save_category_stats(sample_history, test_file)
    print("第 2 关返回：", res2)
    assert res2 == {"中餐": 2, "面食": 1}, f"第 2 关期望 {{'中餐': 2, '面食': 1}}，实际得到 {res2}"
    assert os.path.exists(test_file), "第 2 关未生成 JSON 文件！"
    with open(test_file, "r", encoding="utf-8") as f:
        saved = json.load(f)
    assert saved == {"中餐": 2, "面食": 1}, f"文件内容不对，实际为 {saved}"
    os.remove(test_file)
    print("✅ 第 2 关通过！全部热身通关，可以进入 B 专项小测啦！")
