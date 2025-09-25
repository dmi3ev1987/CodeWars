def up_array(input_array):
    if not input_array:
        return None
    result = []
    value_to_add = 1
    for index in range(len(input_array) - 1, -1, -1):
        if input_array[index] < 0 or input_array[index] > 9:
            return None
        number_to_add = input_array[index] + value_to_add
        if number_to_add == 10:
            result.append(0)
        else:
            result.append(number_to_add)
            value_to_add = 0
    if value_to_add != 0:
        result.append(value_to_add)
    return result[::-1]