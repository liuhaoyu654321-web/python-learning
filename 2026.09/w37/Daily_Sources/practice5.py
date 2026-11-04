import json
data = {
    "name": "Eric",
    "age": 24
}
with open("person.json", "w", encoding= "UTF-8") as file:
    json.dump(data,file,ensure_ascii = False,indent = 2)
with open("person.json", "r",encoding = "utf-8") as file:
    saved_data = json.load(file)
    print(saved_data["name"])