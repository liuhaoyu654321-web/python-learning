from todo import show_todos,add_todo,complete_todo,delete_todo
from storage import load_todos,save_todos

def show_menu():
    print("""----todo 管理器---
    1.查看任务
    2.添加任务
    3.完成任务
    4.删除任务
    5.退出
    """)
todos = load_todos()
while True:
    show_menu()
    choice = input("请输入")
    if choice == "1":
        show_todos(todos)
    elif choice == "2":
        title = input("请输入")
        add_todo(todos,title)
        save_todos(todos)
    elif choice == "3":
        index = int(input("请输入"))
        complete_todo(todos,index)
        save_todos(todos)
    elif choice == "4":
        index = int(input("请输入"))
        delete_todo(todos,index)
        save_todos(todos)
    elif choice == "5":
        break 
