def count_old_enough(users,min_age):

    for user in users:
        if user["age"] >= min_age:
            name = user.get("name")
            print(name)


users = [
    {"name": "Eric", "age": 24},
    {"name": "Tom", "age": 16},
    {"name": "Alice", "age": 30}
]
count_old_enough(users, 18)