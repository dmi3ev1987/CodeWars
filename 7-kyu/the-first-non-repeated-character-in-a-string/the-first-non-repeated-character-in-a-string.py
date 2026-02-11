from collections import Counter


def first_non_repeated(input_string):
    single_chars = [
        key for key, value in Counter(input_string).items() if value == 1
    ]
    first_char = None
    for char in input_string:
        if char in single_chars:
            first_char = char
            break
    return first_char
