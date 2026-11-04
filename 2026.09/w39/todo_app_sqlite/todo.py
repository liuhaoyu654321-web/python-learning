import storage


def show_todos():
    todos = storage.get_todos()

    for todo in todos:
        if todo["completed"]:
            status = "已完成"
        else:
            status = "未完成"

        print(todo["id"], todo["title"], status)
def add_todo(title):
    storage.add_todo(title)        
def complete_todo(todo_id):
    storage.complete_todo(todo_id)    
def delete_todo(todo_id):
    storage.delete_todo(todo_id)    
if __name__ == "__main__":
    show_todos()        