def remove_smallest(input_numbers):
    if len(input_numbers) == 0 or len(input_numbers) == 1:
        return []
    min_number = min(input_numbers)
    for index in range(len(input_numbers)):
        if input_numbers[index] == min_number:
            input_numbers = input_numbers[:index] + input_numbers[index+1:]
            break
    return input_numbers