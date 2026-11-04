import requests
import storage

storage.init_db()
question = input("请输入问题：")

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

session = requests.Session()
session.trust_env = False

response = session.post(
    url,
    json=data
)
if response.status_code == 200:
    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    print(answer)
    storage.save_chat(question, answer) 
    print(storage.get_chats())       
else:
    print("请求失败：", response.status_code)
    print(response.text)
