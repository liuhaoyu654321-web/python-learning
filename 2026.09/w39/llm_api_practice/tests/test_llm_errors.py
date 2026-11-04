
import requests
from unittest.mock import patch

from llm import chat


# 测试 1：模拟网络请求超时
def test_timeout(caplog):
    with patch(
        "llm.requests.post",
        side_effect=requests.Timeout("模拟请求超时")
    ):
        result = chat("测试问题")

    assert result is None
    assert "DeepSeek 请求超时" in caplog.text


# 测试 2：模拟 HTTP 401
def test_http_401(caplog):
    response = requests.Response()
    response.status_code = 401
    response.url = "https://api.deepseek.com/chat/completions"

    with patch("llm.requests.post", return_value=response):
        result = chat("测试问题")

    assert result is None
    assert "401" in caplog.text


# 测试 3：模拟 HTTP 429
def test_http_429(caplog):
    response = requests.Response()
    response.status_code = 429
    response.url = "https://api.deepseek.com/chat/completions"

    with patch("llm.requests.post", return_value=response):
        result = chat("测试问题")

    assert result is None
    assert "429" in caplog.text
