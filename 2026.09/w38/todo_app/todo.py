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