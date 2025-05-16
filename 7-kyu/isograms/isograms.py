from collections import Counter
​
def is_isogram(string):
    for value in Counter(string.lower()).values():
        if value > 1:
            return False
    return True