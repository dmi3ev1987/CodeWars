def matrix(input_array):
    for index in range(len(input_array)):
        input_array[index][index] = 0 if input_array[index][index] < 0 else 1
    return input_array