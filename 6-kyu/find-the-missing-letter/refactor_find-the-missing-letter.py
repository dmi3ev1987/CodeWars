def find_missing_letter(chars):
    for index in range(len(chars) - 1):
        current_letter, next_letter = ord(chars[index]), ord(chars[index + 1])
        if next_letter != current_letter + 1:
            return chr(current_letter + 1)
    return None
