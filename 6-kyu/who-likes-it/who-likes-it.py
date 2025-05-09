def likes(names):
    text = 'likes this' if len(names) <= 1 else 'like this'

    if not names:
        return f'no one {text}'
    if len(names) == 1:
        return f'{names[0]} {text}'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} {text}'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} {text}'

    return f'{names[0]}, {names[1]} and {len(names) - 2} others {text}'
