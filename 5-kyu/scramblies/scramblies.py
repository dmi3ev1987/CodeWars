from collections import Counter


def scramble(s1, s2):
    s1_counts = Counter(s1)
    for letter, count in Counter(s2).items():
        if s1_counts[letter] < count:
            return False
    return True
