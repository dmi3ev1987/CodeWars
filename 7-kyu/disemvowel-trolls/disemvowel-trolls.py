def disemvowel(string_):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ' '.join(
        ''.join(letter for letter in word if letter.lower() not in vowels)
        for word in string_.split(' ')
    )
