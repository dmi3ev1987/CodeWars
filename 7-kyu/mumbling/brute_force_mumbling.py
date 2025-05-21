def accum(inner_string):
    return '-'.join(
        (inner_string[index] * (index + 1)).capitalize()
        for index in range(len(inner_string))
    )
