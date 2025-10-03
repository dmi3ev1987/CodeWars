def longest_repetition(chars):
    current_char = ''
    current_repetition = 0
    result_char = chars[0] if chars else ''
    max_repetition = 1 if chars else 0
    for char in chars:
        if char == current_char:
            current_repetition += 1
            if current_repetition > max_repetition:
                max_repetition = current_repetition
                result_char = char
        if char != current_char:
            current_char = char
            current_repetition = 1
    return result_char, max_repetition
