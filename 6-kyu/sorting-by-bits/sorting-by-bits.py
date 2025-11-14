def sort_by_bit(input_array):
    input_array.sort(key=lambda x: (bin(x).count('1'), x))
    return input_array