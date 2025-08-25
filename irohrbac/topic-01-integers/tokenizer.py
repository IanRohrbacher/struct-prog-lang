import re

patterns = [
    [r"\d*\.\d+ | \d+\.\d* | \d+", "number"], # r -. regx | \d* -> all digits | \d+ -> one gigit | \. -> literal '.'
    [r"\+", "+"],
    [r".", "error"]
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenizer(charters):
    tokens = []
    position = 0
    while position < len(charters):
        #find first matching token
        for pattern, tag, in patterns:
            match = pattern.match(charters, position)
            if match:
                break
    
    assert match

    if tag == "error":
        raise Exception(f"Syntax Error: illegal character : {match.group(0)}")
    
    token = {"tag":tag, "position":position}
    value = match.group(0)
    if token["tag"] == "number":
        if "." in value:
            token["value"] = float(value)
        else:
            token["value"] = int(value)
        tokens.append(token)
        position = match.end()

    tokens.append({"tag":None, "position":position})

    return tokens

def test_simple_tokens():
    print("print simple tokens...")
    assert tokenizer("+") [
        {"tag":"+", "position":0},
        {"tag":None, "position":1}
    ]
    print("first")
    assert tokenizer("3.1") [
        {"tag":"number", "position":0, "value":3.1},
        {"tag":None, "position":1}
    ]
    print("loop?")
    
if __name__ == "__main__":
    print("running main...")

    test_simple_tokens()