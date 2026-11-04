from models import AIResponse

def validate(data):

    try:

        result = AIResponse(**data)

        return result

    except Exception as e:

        print(e)

        return None