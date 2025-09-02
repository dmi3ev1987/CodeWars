def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays or None in array_of_arrays:
        return 0
    lengths = [len(array) for array in sorted(array_of_arrays, key=len)]
    if lengths[0] == 0:
        return 0
    result = lengths[0]
    for length in lengths[1:]:
        result += 1
        if result != length:
            break
    return result
