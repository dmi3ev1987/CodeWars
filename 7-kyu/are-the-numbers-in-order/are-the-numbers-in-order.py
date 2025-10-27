def in_asc_order(input_array):
    current_number = input_array[0]
    for number in input_array[1:]:
        if number < current_number:
            return False
        current_number = number
    return True