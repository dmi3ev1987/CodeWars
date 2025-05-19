def find_short(input_string):
    return min(len(word) for word in input_string.split())
