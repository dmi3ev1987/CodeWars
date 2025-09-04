def thirt(input_number):
    pattern = [1, 10, 9, 12, 3, 4]
    str_number = str(input_number)[::-1]
    result = 0
    patter_index = 0
    for number in str_number:
        result += int(number) * pattern[patter_index]
        patter_index += 1
        if patter_index == len(pattern):
            patter_index = 0
    if input_number != result:
        return thirt(result)
    return result