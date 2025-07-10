def find_missing_letter(chars):
    current_letter = chars[0]
    for letter in chars[1:]:
        if ord(current_letter) + 1 != ord(letter):
            return chr(ord(current_letter) + 1)
        current_letter = letter
    return None
