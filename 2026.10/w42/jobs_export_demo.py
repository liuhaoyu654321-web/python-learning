import sqlite3
import json
from pathlib import Path


db_path = Path(__file__).resolve().parent / "jobs_demo.db"

conn = sqlite3.connect(db_path)

rows = conn.execute("SELECT title, city FROM jobs").fetchall()

conn.close()

jobs = []

for row in rows:
    job = {
        "title": row[0],
        "city": row[1]
    }
    jobs.append(job)

city_counts = {}

for job in jobs:
    city = job["city"]
    city_counts[city] = city_counts.get(city, 0) + 1


payload = {
    "total_jobs": len(jobs),
    "city_counts": city_counts,
    "jobs": jobs
}
file_path = Path(__file__).resolve().parent / "jobs_demo.json"
file_path.write_text(
    json.dumps(payload, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print("导出成功：", file_path)
