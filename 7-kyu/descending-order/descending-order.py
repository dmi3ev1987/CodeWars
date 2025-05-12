def descending_order(numbers):
    numbers_list = [int(number) for number in str(numbers)]
    numbers_list.sort(reverse=True)
    str_list = [str(number) for number in numbers_list]
    return int(''.join(str_list))