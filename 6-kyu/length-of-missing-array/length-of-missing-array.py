def get_length_of_missing_array(array_of_arrays):
    lengths = [
        len(array) if array is not None else 0 for array in array_of_arrays
    ]
    lengths.sort()
    if not lengths or 0 in lengths:
        return 0
    result = lengths[0]
    for index in range(len(lengths) - 1):
        if lengths[index + 1] != lengths[index] + 1:
            return lengths[index] + 1
    return 0
