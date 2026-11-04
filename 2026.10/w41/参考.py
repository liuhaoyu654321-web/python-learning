import sqlite3
import requests


# 1. 初始化数据库
conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
    )
""")


# 2. 用户输入
question = input("请输入问题：")


# 3. LLM API
url = "http://127.0.0.1:1234/v1/chat/completions"

data = {
    "model": "qwen/qwen3.5-9b",
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ]
}


# 4. 发送请求
session = requests.Session()
session.trust_env = False

response = session.post(
    url,
    json=data
)


# 5. 处理模型返回
if response.status_code == 200:
    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    print("模型回答：", answer)


    # 6. 保存到 SQLite
    cursor.execute(
        "INSERT INTO chats (question, answer) VALUES (?, ?)",
        (question, answer)
    )

    conn.commit()


    # 7. 查询验证
    cursor.execute("SELECT * FROM chats")

    rows = cursor.fetchall()

    print("数据库记录：", rows)

else:
    print("请求失败：", response.status_code)
    print(response.text)


# 8. 关闭数据库
conn.close()