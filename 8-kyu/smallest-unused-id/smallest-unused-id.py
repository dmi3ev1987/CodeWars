def next_id(input_array):
    if not input_array:
        return 0
    sorted_array = sorted(set(input_array))
    current = sorted_array[0]
    if current != 0:
        return 0
    for number in sorted_array[1:]:
        if current != number - 1:
            return current + 1
        current = number
    return current + 1