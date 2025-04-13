def narcissistic(value):
    result = 0
    lenght_value = len(str(value))
    for item in str(value):
        result += (int(item)**lenght_value)
    return result == value