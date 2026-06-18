import json

def to_obj(s):
    """
    Converts JSON text from LLM -> Python object
    """
    try:
        return json.loads(s)
    except Exception as e:
        print(f"to_obj parse fail: {e}")
        return {}
