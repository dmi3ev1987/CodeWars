def remove_smallest(input_numbers):
    result = input_numbers[:]
    if result:
        result.remove(min(result))
    return result