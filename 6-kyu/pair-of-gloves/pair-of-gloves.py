from collections import Counter
​
​
def number_of_pairs(gloves):
    glove_counter = Counter(gloves)
    result = 0
    for glove in glove_counter:
        if glove_counter[glove] >= 2:
            result += glove_counter[glove] // 2
    return result