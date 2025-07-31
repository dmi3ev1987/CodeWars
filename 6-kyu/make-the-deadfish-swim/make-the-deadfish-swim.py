def parse(data):
    result = []
    commands = {
        'i': lambda x: x + 1,
        'd': lambda x: x - 1,
        's': lambda x: x * x,
        'o': lambda x: result.append(x) or x,
    }
    value = 0
    for letter in data:
        if letter in commands:
            value = commands[letter](value)
    return result