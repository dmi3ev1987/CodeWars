def sort_vowels(input_string):
    if not isinstance(input_string, str):
        return ''
    return '\n'.join(
        '|' + char
        if char.lower() in 'aeiou'
        else char + '|'
        for char in input_string
        )