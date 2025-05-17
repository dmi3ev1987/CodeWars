def xo(string):
    counter = {
        'x': 0,
        'o': 0,
    }
    for letter in string.lower():
        if letter in counter:
            counter[letter] += 1
    return counter['x'] == counter['o']