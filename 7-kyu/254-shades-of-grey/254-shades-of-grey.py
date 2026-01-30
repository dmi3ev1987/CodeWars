def shades_of_grey(input_number):
    return [
        '#' + format(number, '02x') * 3
        for number in range(1, min(254, input_number) + 1)
    ]