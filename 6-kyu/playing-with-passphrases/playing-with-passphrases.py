def play_pass(input_string, shift_number):
    complement = 9
    positon = 0
    result = ''
    for char in input_string.upper():
        if char.isalpha():
            base = ord('A')
            shifted_code = base + (ord(char) - base + shift_number) % 26
            letter = chr(shifted_code)
            if positon % 2 == 0:
                result += letter.upper()
            else:
                result += letter.lower()
        elif char.isdigit():
            result += str(complement - int(char))
        else:
            result += char
        positon += 1
    return result[::-1]
