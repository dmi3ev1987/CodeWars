def expanded_form(number):
    result = []
    str_number = str(number)
    length = len(str_number)
    for index in range(length):
        if str_number[index] != '0':
            result.append(str_number[index] + (length - 1) * '0')
        length -= 1
    return ' + '.join(result)
