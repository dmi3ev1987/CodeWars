def abbreviate(input_string):
    result = ''
    part_word = ''
    for letter in input_string:
        if letter.isalpha():
            part_word += letter
        else:
            if len(part_word) > 3:
                part_word = (
                    part_word[0] + str(len(part_word) - 2) + part_word[-1]
                )
            result += part_word + letter
            part_word = ''
    if len(part_word) > 3:
        part_word = part_word[0] + str(len(part_word) - 2) + part_word[-1]
    result += part_word
    return result
