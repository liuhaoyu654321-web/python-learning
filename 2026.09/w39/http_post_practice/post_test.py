import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "学习 POST",
    "body": "这是我第一次发送 POST 请求",
    "userId": 1
}

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.post(
    url,
    headers=headers,
    json=data
)
print(response.status_code)
print(response.json())
print(response.request.headers["Authorization"])