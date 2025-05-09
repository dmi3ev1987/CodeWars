def high_and_low(numbers):
    numbers_list = numbers.split(' ')
    min_number = max_number = int(numbers_list[0])
    for number in numbers_list:
        min_number = min(min_number, int(number))
        max_number = max(max_number, int(number))
    return f'{max_number} {min_number}'