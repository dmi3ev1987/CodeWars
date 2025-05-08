def rot13(message):
    result = []
    shift = 13
    for letter in message:
        if 'a' <= letter <= 'z':
            result.append(
                chr(get_shifted_ord_number(ord('a'), ord(letter), shift)),
            )
        elif 'A' <= letter <= 'Z':
            result.append(
                chr(get_shifted_ord_number(ord('A'), ord(letter), shift)),
            )
        else:
            result.append(letter)
    return ''.join(result)


def get_shifted_ord_number(ord_start, ord_letter, shift):
    return ord_start + ((ord_letter - ord_start + shift) % 26)
