import re
​
​
def solve(input_string):
    """Split each individual vowel (a, e, i, o, u).
​
    Square brackets [] in `re.split` make it a character class.
    Example: re.split('[aeiou]', 'hello world') splits at 'e' and 'o'.
    """
    return max(
        sum(ord(letter) - ord('a') + 1 for letter in chunk)
        for chunk in re.split('[aeiou]', input_string)
    )