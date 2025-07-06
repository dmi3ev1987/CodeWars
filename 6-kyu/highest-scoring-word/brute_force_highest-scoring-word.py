def high(input_string):
    score = [
        sum(ord(letter.lower()) - ord('a') + 1 for letter in word)
        for word in input_string.split()
    ]
    return input_string.split()[score.index(max(score))]
