def max_product(input_array):
    max_1, max_2 = 0, 0
    for number in input_array:
        if number > max_1:
            max_2 = max_1
            max_1 = number
        elif number > max_2:
            max_2 = number
    return max_1 * max_2
