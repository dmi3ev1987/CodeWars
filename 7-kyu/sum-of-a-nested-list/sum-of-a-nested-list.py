def sum_nested(input_list):
    total = 0
    for value in input_list:
        if type(value) == list:
            total += sum_nested(value)
        else:
            total += value
    return total