def lowercase_count(input_string):
    count = 0
    for letter in input_string:
        if letter.islower():
            count += 1
    return count