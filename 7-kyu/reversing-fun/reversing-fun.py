def reverse_fun(input_string: str) -> str:
    reversed_string = input_string[::-1]
    result_string = []
    for index in range(len(input_string)):
        result_string.append(reversed_string[0])
        reversed_string = reversed_string[1:][::-1]
    return ''.join(result_string)
