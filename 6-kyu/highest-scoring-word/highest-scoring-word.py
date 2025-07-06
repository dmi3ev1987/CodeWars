def high(input_string):
    return max(
        input_string.split(),
        key=lambda word: sum(ord(letter) - 96 for letter in word),
    )
