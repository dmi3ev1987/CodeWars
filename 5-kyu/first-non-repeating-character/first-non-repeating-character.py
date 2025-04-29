def first_non_repeating_letter(s):
    no_reapet_letter = ''
    for letter in s:
        if s.lower().count(letter.lower()) == 1:
            no_reapet_letter = letter
            break
    return no_reapet_letter
​