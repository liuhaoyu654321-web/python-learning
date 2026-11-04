import storage
import todo


def show_menu():
    print("""
--- Todo 管理器 ---
1. 查看任务
2. 添加任务
3. 完成任务
4. 删除任务
5. 退出
""")


storage.init_db()

while True:
    show_menu()

    choice = input("请输入：")

    if choice == "1":
        todo.show_todos()

    elif choice == "2":
        title = input("请输入任务：")
        todo.add_todo(title)

    elif choice == "3":
        todo_id = int(input("请输入任务 ID："))
        todo.complete_todo(todo_id)

    elif choice == "4":
        todo_id = int(input("请输入任务 ID："))
        todo.delete_todo(todo_id)

    elif choice == "5":
        break

    else:
        print("请输入 1-5")