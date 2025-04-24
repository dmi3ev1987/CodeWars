def rot13(message):
    result = []
    shift = 13
    for letter in message:
        if 'a' <= letter <= 'z':
            ord_start = ord('a')
            result.append(
                chr(get_shifted_ord_number(ord_start, ord(letter), shift))
            )
        elif 'A' <= letter <= 'Z':
            ord_start = ord('A')
            result.append(
                chr(get_shifted_ord_number(ord_start, ord(letter), shift))
            )
        else:
            result.append(letter)
    return ''.join(result)
​
​
def get_shifted_ord_number(ord_start, ord_letter, shift):
    return ((ord_letter - ord_start + shift) % 26) + ord_start
​