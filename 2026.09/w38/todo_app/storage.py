import json
from pathlib import Path
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "todos.json"
def load_todos():
    with open("DATA_FILE","r",encoding= "utf-8")as f:
        data = json.load(f)
        return data

def save_todos(todos):
    with open("DATA_FILE","w",encoding="utf-8")as f:
        json.dump(todos,f,ensure_ascii = False,indent = 4)


