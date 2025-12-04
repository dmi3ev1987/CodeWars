def reverse_number(input_number):
    result = int(str(input_number)[::-1].strip('-'))
    return result if input_number >= 0 else -result