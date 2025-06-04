def printer_error(input_string):
    count = 0
    for letter in input_string:
        if 'm' < letter <= 'z':
            count += 1
    return f'{count}/{len(input_string)}'
