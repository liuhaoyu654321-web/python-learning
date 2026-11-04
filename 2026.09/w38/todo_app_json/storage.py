import json
from pathlib import Path
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "todos.json"
def load_todos():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("错误：todos.json 内容损坏，请检查文件")
        raise

    return data

def save_todos(todos):
    with open(DATA_FILE,"w",encoding="utf-8")as f:
        json.dump(todos,f,ensure_ascii = False,indent = 4)


