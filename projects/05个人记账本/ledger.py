# 个人记账本 V1（极简示范版：记一笔、看明细与分类汇总、JSON 永久存盘）
# 【看懂优先级】🔴 现在要看懂｜🟡 看大意就行｜🟢 现在完全不用管
import json, os
from datetime import datetime
BILLS_FILE = os.path.join(os.path.dirname(__file__), "bills.json")  # 🟢 账单文件路径
# 🟡 看大意就行：读取与保存 JSON 账单
def load_bills():
    if not os.path.exists(BILLS_FILE):
        return []
    with open(BILLS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def save_bills(bills):
    with open(BILLS_FILE, "w", encoding="utf-8") as f:
        json.dump(bills, f, ensure_ascii=False, indent=2)
# 🔴 现在要看懂：用 range(len(bills)) 编号展示，并统计总花销与分类
def show_summary(bills):
    if not bills:
        print("还没有账单记录哦。")
        return
    total = 0
    by_cat = {}
    for i in range(len(bills)):  # 🔴 1.4 重点：i 从 0 开始，显示编号用 i + 1
        b = bills[i]
        print(f"{i + 1}. [{b['date']}] {b['category']} - {b['note']}：{b['amount']}元")
        total += b["amount"]
        by_cat[b["category"]] = by_cat.get(b["category"], 0) + b["amount"]
    print(f"--- 合计：{total:.2f} 元｜分类：{by_cat} ---")
# 🔴 现在要看懂：主菜单循环（1 记一笔 / 2 看明细 / q 退出）
def main():
    bills = load_bills()
    while True:
        cmd = input("\n=== 个人记账本 ===\n1.记一笔  2.看明细与汇总  q.退出\n请选择: ").strip().lower()
        if cmd == "q":
            break
        if cmd == "1":
            cat = input("分类（回车默认 餐饮）: ").strip() or "餐饮"
            note = input("备注（如 午饭拉面）: ").strip() or "未填"
            amt = input("金额（数字）: ").strip()
            if not amt.replace(".", "", 1).isdigit():  # 🟡 简单校验是否为正数
                print("金额请输入数字哦。")
                continue
            today = datetime.now().strftime("%Y-%m-%d")  # 🟢 自动获取今天日期
            bills.append({"date": today, "category": cat, "note": note, "amount": float(amt)})
            save_bills(bills)
            print("已记账并保存！")
        elif cmd == "2":
            show_summary(bills)
# 🟢 完全不用管：Python 固定启动入口
if __name__ == "__main__":
    main()
