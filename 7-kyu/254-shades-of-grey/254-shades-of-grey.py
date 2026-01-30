def shades_of_grey(input_number):
    if input_number > 254:
        input_number = 254
    return ['#' + format(number, '02x') * 3 for number in range(1, input_number + 1)]