def thirt(input_number):
    pattern = [1, 10, 9, 12, 3, 4]
    result = sum(
        int(number) * pattern[index % 6]
        for index, number in enumerate(reversed(str(input_number)))
    )
    if result == input_number:
        return result
    return thirt(result)