def title_to_number(title):
    result = 0
    multiplier = 1
    for number in [ord(letter.lower()) - 96 for letter in title][::-1]:
        result += number * multiplier
        multiplier *= 26
    return result
