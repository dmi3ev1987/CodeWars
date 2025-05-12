def descending_order(numbers):
    numbers_list = list(str(numbers))
    return int(''.join(reversed(sorted(numbers_list))))
​