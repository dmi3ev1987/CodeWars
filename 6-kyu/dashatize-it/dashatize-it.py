def dashatize(input_number):
    result = []
    str_number = str(input_number).strip('-')
    digit_to_add = ''
    for digit in str_number:
        if int(digit) % 2:
            if digit_to_add:
                result.append(digit_to_add)
                digit_to_add = ''
            result.append(digit)
        else:
            digit_to_add += digit
    if digit_to_add:
        result.append(digit_to_add)
    return '-'.join(result)