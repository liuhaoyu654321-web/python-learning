todos = [
    {"title": "学习Python", "completed": True},
    {"title": "健身", "completed": False},
    {"title": "看书", "completed": True}
]
def count_completed(todos):
    count_completed = 0
    for todo in todos:
        if todo["completed"] == True:
            count_completed += 1
    return count_completed
result = count_completed(todos)
print(result)    
        