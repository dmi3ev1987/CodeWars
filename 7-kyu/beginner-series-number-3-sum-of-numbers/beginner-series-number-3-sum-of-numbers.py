def get_sum(a, b):
    if a == b:
        return a
    if a > b:
        a, b = b, a
    number_sum = 0
    for number in range(a, b + 1):
        number_sum += number
    return number_sum