def negation_value(s: str, val) -> bool:
    result = val
    for char in s:
        if result:
            result = False
        else:
            result = True
    return result