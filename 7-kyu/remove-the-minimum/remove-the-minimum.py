def remove_smallest(input_numbers):
    if len(input_numbers) < 1:
        return input_numbers
    index = input_numbers.index(min(input_numbers))
    return input_numbers[:index] + input_numbers[index + 1 :]
