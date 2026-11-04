import json
import requests
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

question = input("请输入问题：")

url = "http://127.0.0.1:1234/v1/chat/completions"

data = {
    "model": "qwen/qwen3.5-9b",

    "messages": [
        {
            "role": "user",
            "content": f"""
请分析下面这条用户需求：

{question}

summary：用一句话总结用户真正想解决的问题。
category：填写简短的问题类型。
urgent：如果需要尽快处理填写 true，否则填写 false。
confidence：填写 0 到 1 之间的数字，表示你对 category 分类结果的置信度。

只填写最终结果，不要解释分析过程。
"""
}
    ],

    "response_format": {
        "type": "json_schema",
        "json_schema": {
            "name": "question_analysis",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "summary": {
                        "type": "string"
                    },
                    "category": {
                        "type": "string"
                    },
                    "confidence":{
                        "type": "number",
                        "minimum":0,
                        "maximum": 1
                    },
                    "urgent":{
                        "type": "boolean"
                    }
                    
                },
                "required": [
                    "summary",
                    "category",
                    "urgent",
                    "confidence"
                ],
                "additionalProperties": False
            }
        }
    }
    }

session = requests.Session()
session.trust_env = False

response = session.post(
    url,
    json=data
)

result = response.json()
content = result["choices"][0]["message"]["content"]

try:
    parsed = json.loads(content)

    logging.info(f"总结: {parsed['summary']}")
    logging.info(f"类型: {parsed['category']}")
    logging.info(f"紧急: {parsed['urgent']}")
    logging.info(f"置信度: {parsed['confidence']}")

except json.JSONDecodeError:
    print("JSON 解析失败")
    print("模型原始返回：", content)