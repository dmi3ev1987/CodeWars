def sort_vowels(input_string):
    return (
        ''
        if not isinstance(input_string, str)
        else '\n'.join(
            '|' + char if char.lower() in 'aeiou' else char + '|'
            for char in input_string
        )
    )