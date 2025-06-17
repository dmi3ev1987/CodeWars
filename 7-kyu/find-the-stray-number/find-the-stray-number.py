def stray(input_array):
    if input_array.count(input_array[0]) == 1:
        return input_array[0]
    for number in input_array:
        if number != input_array[0]:
            return number
    return None
