def get_count(sentence):
    vowels = {'a', 'e', 'o', 'i', 'u'}
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count