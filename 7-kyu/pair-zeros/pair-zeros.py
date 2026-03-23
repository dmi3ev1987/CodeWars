def pair_zeros(input_array):
    result = []
    zero = False
    index = 0
    for item in input_array:
        if zero and item == 0:
            zero = False
            continue
        elif item == 0:
            zero = True
        result.append(item)
    return result
