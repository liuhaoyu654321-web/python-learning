jobs = [
    {"title": "Python开发", "city": "西安"},
    {"title": "AI开发", "city": "北京"},
    {"title": "自动化工程师", "city": "西安"}
]

city_counts = {}
for job in jobs:
    city = job["city"]
    city_counts[city] = city_counts.get(city,0) + 1

print (city_counts)