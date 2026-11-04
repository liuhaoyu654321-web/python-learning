import logging

from llm import chat
from parser import parse_json
from validator import validate
from logger_config import setup_logger
from storage import init_db, save_analysis

def main():
    # 1. 配置日志
    setup_logger()
    init_db()

    # 2. 用户输入
    question = input("请输入问题：")

    # 3. 调用 LLM
    content = chat(question)

    if not isinstance(content, str):
        logging.error("LLM 没有返回有效文本")
        return

    # 4. 解析 JSON
    data = parse_json(content)

    if not isinstance(data, dict):
        logging.error("JSON 解析失败或返回的不是对象")
        return

    # 5. Pydantic 数据校验
    result = validate(data)

    if result is None:
        logging.error("Pydantic 数据校验失败")
        return

    save_analysis(question, result)
    # 6. 输出结果
    logging.info("数据处理成功")
    logging.info("总结：%s", result.summary)
    logging.info("分类：%s", result.category)
    logging.info("紧急：%s", result.urgent)
    logging.info("置信度：%s", result.confidence)


if __name__ == "__main__":
    main()