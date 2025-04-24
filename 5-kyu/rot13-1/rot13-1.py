def rot13(message):
    result = []
    for letter in message:
        if 'a' <= letter <= 'z':
            result.append(chr(((ord(letter) - ord('a') + 13) % 26) + ord('a')))
        elif 'A' <= letter <= 'Z':
            result.append(chr(((ord(letter) - ord('A') + 13) % 26 + ord('A'))))
        else:
            result.append(letter)
    return ''.join(result)
​