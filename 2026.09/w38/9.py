import json

def show_todos(todos):
    for index,todo in enumerate(todos,start =1):
        titles = todo["title"]
        if todo["completed"] == True:
            print(index,titles, "- 已完成")
        else:
            print(index,titles, "- 未完成")

def add_todo(todos, title):
    todo = {
        "title": title,
        "completed": False
    }

    todos.append(todo)   

def complete_todo(todos,index):
    index = index - 1
    for i,todo in enumerate(todos):
        if i == index:
            todo["completed"] = True
            break

def delete_todo(todos,index):
    index = index - 1
    todos.pop(index)

def load_todos():
    with open("todos.json","r",encoding= "utf-8")as f:
        data = json.load(f)
        return data

def save_todos(todos):
    with open("todos.json","w",encoding="utf-8")as f:
        json.dump(todos,f,ensure_ascii = False,indent = 4)

def show_menu():
    print(
        """=====Todo管理器=====

        1.查看任务
        2.添加任务
        3.完成任务
        4.删除任务
        5.退出
    """
    )

todos = load_todos()
while True:
    show_menu()

    choice = input("请选择:")

    if choice == "1":
       show_todos(todos)
    elif choice == "2":
       title = input("请输入任务:")
       add_todo(todos,title)
       save_todos(todos)
    elif choice == "3":
       index = int(input("请输入完成任务编号:"))
       complete_todo(todos,index)
       save_todos(todos)
    elif choice == "4":
       index = int(input("请输入删除任务编号:"))
       delete_todo(todos,index)
       save_todos(todos)   
    elif choice == "5":
       break

                   

