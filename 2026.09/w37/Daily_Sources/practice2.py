import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos"
)

data = response.json()
count = 0
for todo in data:
    if todo["completed"] == False:
        print(todo["title"])
        count = count + 1

print(response.status_code)
print(count)