def up_array(input_array):
    if not input_array or any(number > 9 or number < 0 for number in input_array):
        return None
    result = []
    value_to_add = 1
    for index in range(len(input_array) - 1, -1, -1):
        number_to_add = input_array[index] + value_to_add
        if number_to_add > 9:
            result.append(0)
        else:
            result.append(number_to_add)
            value_to_add = 0
    if value_to_add:
        result.append(value_to_add)
    return result[::-1]