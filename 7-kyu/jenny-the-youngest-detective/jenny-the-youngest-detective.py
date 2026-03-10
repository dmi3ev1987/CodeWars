def missing(input_numbers, input_string):
    sorted_numbers = sorted(input_numbers)
    stripped_string = input_string.replace(' ', '')
    if sorted_numbers[-1] > len(stripped_string) - 1:
        return 'No mission today'
    result = ''
    for index in sorted_numbers:
        result += stripped_string[index]
    return result.lower()