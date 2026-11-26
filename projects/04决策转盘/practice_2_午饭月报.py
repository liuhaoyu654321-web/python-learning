# 🟡 手写练习 2：给决策转盘加「午饭月报」功能（读你真实的 data.json，生成一份报告）
# 【看懂优先级】🔴 现在要看懂（核心基本功）｜🟡 看大意就行（先不抠细节）｜🟢 现在完全不用管（工具套话，跳过）
#
# 玩法：5 个函数全是空的，从空白开始写（不翻旧代码、不看答案）。
#       每写完一个就运行一次：python practice_2_午饭月报.py
#       全部 ✅ 后，程序会用你真实的抽签记录生成「午饭月报」并存成 午饭月报.json。
# 套路提醒（只提醒这一次）：建空容器 → for 循环加工 → 循环外 return
# 记录：每题注明 ✅ 独立 / 🟡 第几级提示，写在函数末尾的 # 记录： 后面

import json


# 🔴 第 1 题：一共花了多少钱
def total_spent(history):
    """history 是抽签记录列表，每条形如 {"name": "黄焖鸡米饭", "category": "中餐", "price": 24, ...}
    返回所有记录 price 的总和。
    例：[{"price": 24}, {"price": 18}] → 42；空列表 [] → 0
    """
    # TODO
    total_price = 0
    for s in history:
        total_price += s["price"]
    return total_price    
    # 记录：🟡 第 2 级提示


# 🔴 第 2 题：预算内能吃什么
def names_under(items, budget):
    """items 是选项列表，每条形如 {"name": "兰州牛肉拉面", "price": 18, ...}
    返回所有 price <= budget 的菜名（只要名字）组成的列表，顺序不变。
    例：[{"name": "A", "price": 18}, {"name": "B", "price": 30}]，budget=20 → ["A"]
    """
    # TODO
    name = []
    for item in items:
        if item["price"] <= budget:
            name.append(item["name"])
    return name       
    # 记录：


# 🔴 第 3 题：每个分类一共花了多少钱
def spent_by_category(history):
    """返回字典 {分类: 该分类总花费}。
    例：[{"category": "中餐", "price": 24}, {"category": "中餐", "price": 22}, {"category": "面食", "price": 18}]
        → {"中餐": 46, "面食": 18}
    """
    # TODO
    spend = {}
    for s in history:
        cat = s["category"]
        spend[cat] = spend.get(cat,0) + s["price"]
    return spend    
    # 记录：🟡 挖空模式（第 1 级提示）


# 🔴 第 4 题：每个标签出现几次（提示：一条选项有好几个标签，循环里还要再套一层循环）
def count_by_tag(items):
    """items 每条形如 {"name": "...", "tags": ["热乎", "管饱"]}
    返回字典 {标签: 出现次数}。
    例：[{"tags": ["热乎", "管饱"]}, {"tags": ["热乎"]}] → {"热乎": 2, "管饱": 1}
    """
    # TODO
    time = {}
    for item in items:
        tags = item["tags"]
        for tag in tags:
            time[tag] = time.get(tag,0) +1
    return time        
    # 记录：🟡 挖空模式（第 1 级提示）


# 🔴 第 5 题：把报告存成 JSON 文件（中文不乱码、带缩进）
def save_report(report, filepath):
    """report 是一个字典，filepath 是文件名字符串（如 "午饭月报.json"）。
    把 report 写进 filepath，什么都不用返回。
    """
    # TODO
    with open(filepath,"w", encoding= "utf-8") as f:
        json.dump(report,f,ensure_ascii= False,indent= 2)
    # 记录：


# ===================== 以下是自动检查 + 生成月报，不用改 =====================
# 🟢 现在完全不用管：下面是测试外壳
def check(no, func, args, expected):
    try:
        got = func(*args)
    except Exception as e:  # 报错了也不让程序崩，先把错误类型打出来
        print(f"❌ 第 {no} 题报错：{type(e).__name__}: {e}")
        return False
    ok = got == expected
    print(f"{'✅' if ok else '❌'} 第 {no} 题：期望 {expected}，实际 {got}")
    return ok


if __name__ == "__main__":
    h = [{"category": "中餐", "price": 24}, {"category": "中餐", "price": 22}, {"category": "面食", "price": 18}]
    it = [{"name": "A", "price": 18, "tags": ["热乎", "管饱"]}, {"name": "B", "price": 30, "tags": ["热乎"]}]
    results = [
        check(1, total_spent, (h,), 64) and check(1, total_spent, ([],), 0),
        check(2, names_under, (it, 20), ["A"]),
        check(3, spent_by_category, (h,), {"中餐": 46, "面食": 18}),
        check(4, count_by_tag, (it,), {"热乎": 2, "管饱": 1}),
    ]
    if all(results):
        data = json.load(open("data.json", encoding="utf-8"))
        report = {
            "总花费": total_spent(data["history"]),
            "各分类花费": spent_by_category(data["history"]),
            "25元内能吃": names_under(data["items"], 25),
            "标签统计": count_by_tag(data["items"]),
        }
        save_report(report, "午饭月报.json")
        try:
            print("\n🎉 第 5 题 ✅，你的午饭月报：")
            print(open("午饭月报.json", encoding="utf-8").read())
        except FileNotFoundError:
            print("\n❌ 第 5 题：没找到 午饭月报.json，文件还没写出来")
    else:
        print(f"\n还差 {results.count(False)} 题，月报生成不了，继续加油～")
