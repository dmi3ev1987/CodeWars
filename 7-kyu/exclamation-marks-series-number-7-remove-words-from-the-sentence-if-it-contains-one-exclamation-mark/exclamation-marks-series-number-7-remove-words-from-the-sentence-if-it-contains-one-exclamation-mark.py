def remove(input_string):
    return ' '.join(word for word in input_string.split() if word.count('!') != 1)