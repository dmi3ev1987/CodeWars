from collections import Counter

KEYPAD = {
    '1ADGJMPTW*# ': 1,
    'BEHKNQUX0': 2,
    'CFILORVY': 3,
    'SZ234568': 4,
    '79': 5,
}


def presses(phrase):
    letter_count = Counter(phrase.upper())
    result = 0
    for letter, number in letter_count.items():
        for button, value in KEYPAD.items():
            if letter in button:
                result += number * value
                break
    return result
