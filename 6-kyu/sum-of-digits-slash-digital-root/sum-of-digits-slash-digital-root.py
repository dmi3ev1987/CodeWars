def digital_root(n):
    if n < 10:
        return n
    result = 0
    for item in str(n):
        result += int(item)
    if len(str(result)) > 1:
        result = digital_root(result)
    return result
​