import json



def parse_json(content):

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        print("JSON解析失败")
        return None