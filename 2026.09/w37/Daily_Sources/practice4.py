import requests
import json
try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(response.status_code)
    if response.status_code== 200:
        data = response.json()
        with open("user.json", "w", encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii=False,indent=2)
        with open("user.json","r", encoding="utf-8") as files:
            saved_data = json.load(files)
            print(saved_data["title"])    
    else:
        print("请求失败")
except requests.exceptions.RequestException:
    print("网络异常")            

