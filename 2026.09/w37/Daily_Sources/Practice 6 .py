import json
import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    if response.status_code == 200:
       data = response.json()

       def count_todos(data):
        completed_count = 0
        unfinished_count = 0

        for todo in data:
           if todo["completed"] == True:
             completed_count += 1
           elif todo["completed"] == False:
             unfinished_count += 1
        return completed_count,unfinished_count
       completed_count, unfinished_count = count_todos(data)   
       print("总任务：", len(data))
       print("已完成：", completed_count)
       print("未完成：", unfinished_count)
       
       with open("todos.json", "w", encoding = "utf-8") as f:
          json.dump(data,f,ensure_ascii = False,indent =2)
    else:
        print("状态码错误")
except requests.exceptions.RequestException:
    print("网络异常")

