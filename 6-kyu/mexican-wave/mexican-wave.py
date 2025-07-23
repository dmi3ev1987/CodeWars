def wave(people):
    return [
        people[:index] + letter.upper() + people[index + 1 :]
        for index, letter in enumerate(people)
        if letter.isalpha()
    ]