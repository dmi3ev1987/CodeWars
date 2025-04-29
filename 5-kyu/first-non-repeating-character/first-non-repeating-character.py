def first_non_repeating_letter(s):
    for letter in s:
        if s.lower().count(letter.lower()) == 1:
            return letter
    return ''