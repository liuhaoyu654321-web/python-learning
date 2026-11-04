import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = response.json()

def count_completed(todos):
    count = 0
    for todo in todos:
       if todo["completed"] == True:
           count += 1

    return count
result = count_completed(data)
print(response.status_code)
print(result)
