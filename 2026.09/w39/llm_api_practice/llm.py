import os
import logging
from pathlib import Path

import requests
from dotenv import load_dotenv


# 读取项目目录下的 .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def chat(question):
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    model = os.getenv("DEEPSEEK_MODEL")

    # 1. 检查配置
    if not api_key or not base_url or not model:
        logging.error("DeepSeek API 配置不完整")
        return None

    # 2. API 地址
    url = base_url.rstrip("/") + "/chat/completions"

    # 3. 请求头：携带身份认证
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 4. 请求内容
    data = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "请分析用户的问题，并且只返回 JSON 对象。"
                    "不要输出 Markdown 或其他文本。\n"
                    "JSON 格式示例：\n"
                    '{"summary":"问题总结",'
                    '"category":"技术问题",'
                    '"urgent":true,'
                    '"confidence":0.95}\n'
                    "summary 和 category 是字符串，"
                    "urgent 是布尔值，"
                    "confidence 是 0 到 1 的数字。"
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "thinking": {"type": "disabled"},
        "response_format": {"type": "json_object"},
        "max_tokens": 500,
        "stream": False
    }

    # 5. 发送请求
    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=(10, 130)
        )

        response.raise_for_status()

    except requests.Timeout:
        logging.error("DeepSeek 请求超时")
        return None

    except requests.HTTPError as e:
        status = e.response.status_code
        logging.error("DeepSeek HTTP 错误：%s", status)
        return None

    except requests.RequestException as e:
        logging.error("网络错误：%s", type(e).__name__)
        return None

    # 6. 处理 API 返回
    try:
        result = response.json()
        content = result["choices"][0]["message"]["content"]

    except (ValueError, KeyError, IndexError, TypeError) as e:
        logging.error("API 返回结构异常：%s", type(e).__name__)
        return None

    if not isinstance(content, str) or not content.strip():
        logging.error("模型返回的正文为空或不是字符串")
        return None

    # 7. 查看 Token 用量
    usage = result.get("usage")

    if isinstance(usage, dict):
        logging.info("Token 用量：%s", usage)

    # 8. 返回正文给 main.py
    return content
