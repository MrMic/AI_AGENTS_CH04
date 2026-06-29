import json
from typing import Any


def to_obj(s) -> Any:
    """
    Converts JSON text from LLM -> Python object
    """
    try:
        return json.loads(s)
    except Exception as e:
        print(f"to_obj parse fail: {e}")
        return {}
