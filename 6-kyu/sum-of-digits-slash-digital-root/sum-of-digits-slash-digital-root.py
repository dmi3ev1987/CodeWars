def digital_root(n):
    str_number = str(n)
    result = 0
    if len(str_number) == 1:
        return n
    while len(str_number) != 1:
        if result != 0:
            result = 0
        for item in str_number:
            result += int(item)
        str_number = str(result)
    return result
​