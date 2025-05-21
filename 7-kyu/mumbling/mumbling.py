def accum(inner_string):
    return '-'.join(
        letter.upper() + letter.lower() * index
        for index, letter in enumerate(inner_string)
    )
