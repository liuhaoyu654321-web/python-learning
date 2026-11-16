import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "assets.json"

DEFAULT_ASSETS = [
    {"name": "银行存款", "category": "现金", "price": 27000},
    {"name": "Sony ZV-E10 II", "category": "摄影", "price": 5200},
    {"name": "Mac 电脑", "category": "数码", "price": 6500},
]

def load_assets():
    if not DATA_FILE.exists():
        return DEFAULT_ASSETS
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def save_assets(assets):
    text = json.dumps(assets, ensure_ascii=False, indent=2)
    DATA_FILE.write_text(text, encoding="utf-8")

def calc_total(assets):
    total = 0
    for item in assets:
        total = total + item["price"]
    return total

def show_board(assets):
    print("\n=== 💰 我的全资产身家看板 ===")
    for i, item in enumerate(assets, start=1):
        print(f"{i}. [{item['category']}] {item['name']}：¥{item['price']}")
    print(f"👉 当前总身家：¥{calc_total(assets)}\n")

assets = load_assets()
while True:
    choice = input("1.查看身家  2.添加资产  3.退出 > ")
    if choice == "1":
        show_board(assets)
    elif choice == "2":
        name = input("物品名称：")
        category = input("分类（现金/数码/摄影等）：")
        price = int(input("估值金额（元）："))
        assets.append({"name": name, "category": category, "price": price})
        save_assets(assets)
        print("✅ 已加入身家！")
    elif choice == "3":
        break
