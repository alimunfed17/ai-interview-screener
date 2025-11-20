import json
import re

def extract_json(text: str):
    if not text:
        return None
    
    text = re.sub(r"```(?:json)?", "", text).strip()

    stack = []
    start = None

    for i, char in enumerate(text):
        if char == "{":
            if start is None:
                start = i
            stack.append("{")

        elif char == "}":
            if stack:
                stack.pop()
                if not stack:
                    candidate = text[start:i+1]
                    try:
                        return json.loads(candidate)
                    except json.JSONDecodeError:
                        pass

    return None
