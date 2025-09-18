def kebabize(input_string):
    return ''.join(
        letter
        if letter.islower()
        else ('-' + letter.lower() if letter.isupper() else '')
        for letter in input_string
    ).strip('-')
