def expanded_form(number):
    return ' + '.join(
        digit + '0' * (len(str(number)) - index - 1)
        for index, digit in enumerate(str(number))
        if digit != '0'
    )