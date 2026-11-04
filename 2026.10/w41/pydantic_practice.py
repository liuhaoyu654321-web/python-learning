from parser import parse_json
from validator import validate


content = """
{
    "summary": "数据库连接失败",
    "category": "database",
    "urgent": true,
    "confidence": 0.95
}
"""


data = parse_json(content)

if data is None:
    print("JSON 解析失败，停止处理")

else:
    result = validate(data)

    if result is None:
        print("数据校验失败，停止处理")

    else:
        print("数据可以继续使用：")
        print(result)