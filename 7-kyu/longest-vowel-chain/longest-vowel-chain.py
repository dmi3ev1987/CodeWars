def solve(s):
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    max_lenght = 0
    for letter in s:
        if letter not in vowels:
            count = 0
        else:
            count += 1
            max_lenght = max(max_lenght, count)
    return max_lenght
