def binary_array_to_number(array):
    return int(''.join(str(number) for number in array), 2)