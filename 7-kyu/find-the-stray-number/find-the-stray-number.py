def stray(input_array):
    unique = input_array[0] if input_array[0] != input_array[1] else input_array[-1]
    for index in range(1, len(input_array) - 1):
        if input_array[index - 1] != input_array[index] and input_array[index + 1] != input_array[index]:
            unique = input_array[index]
            break
    return unique