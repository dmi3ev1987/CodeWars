def deep_count(input_array):
    result = len(input_array)
    for item in input_array:
        if isinstance(item, list):
            result += deep_count(item)
    return result