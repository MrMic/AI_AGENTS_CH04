import json

def to_obj(s):
    """
    Converts JSON text from LLM -> Python object
    """
    try:
        return json.load(s)
    except Exception:
        return {}
