import json
def count_todos(data):
    completed_count = 0
    unfinished_count = 0
    for todo in data:
        if todo["completed"] == True:
           completed_count += 1
        elif todo["completed"] == False:
            unfinished_count += 1
    return {
    "total": len(data),
    "completed": completed_count,
    "unfinished": unfinished_count
    }
try:
    with open("todos.json", "r", encoding="utf-8")as f:
        data = json.load(f)
    result = count_todos(data)
    print(result) 
    with open("todo_summary.json","w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=4)
except FileNotFoundError:
        print("文件不存在")
except json.JSONDecodeError:
        print("json格式错误")
