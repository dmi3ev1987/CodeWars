def reverse_letter(input_string):
    return ''.join(letter for letter in input_string if letter.isalpha())[::-1]
