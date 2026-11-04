import sqlite3
import requests

conn = sqlite3.connect("chat.db")
cursor =  conn.cursor()#

conn.execute(
    """
    CREATE TABLE IF NOT EXEISTS chat ( #
    id INTEGER PRIMARY KEY ,  #
    question TEXT,
    answer TEXT

    )
"""
)

question = input("请输入问题")#

url = "http://127.0.0.1:1234/v1/chat/completions"

data = {
    "model":"qwen/qwen3.5-9b",#
    "message":[
        {
        "role":"user",
        "content":question
        }
    ]
}

#发送请求
session = requests.Session()
session.trust_env = False

response = session.post(
    url,
    json= data
)

if response.status_code == 200:
    result = response.json()
    answer = result["chioces"][0]["message"]["content"]
    print("模型回答：",answer)
    cursor.execute(
        "INSERT INTO chats(question,answer) VALUES(?,?)",
        (question,answer) 
    )

    cursor.execute(
        "SELECT * FROM chats"
    )
    rows = cursor.fetchall()
    print("数据库记录：",rows)
else:
    print("请求失败")    
    print(response.text)

conn.close()    