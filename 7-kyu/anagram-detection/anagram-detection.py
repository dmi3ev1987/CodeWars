from collections import Counter
​
def is_anagram(test, original):
    if len(test) != len(original):
        return False
    return Counter(test.lower()) == Counter(original.lower())