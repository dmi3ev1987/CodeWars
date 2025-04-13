def narcissistic(value):
    str_value = str(value)
    length = len(str_value)
    return sum(int(item) ** length for item in str_value) == value
​