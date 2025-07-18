BRACES = {
    '{': '}',
    '[': ']',
    '(': ')',
}
​
​
def valid_braces(string):
    index = 0
    while len(string) >= 2:
        if index == len(string) - 1 or string[index] not in BRACES:
            return False
        if BRACES[string[index]] == string[index + 1]:
            string = string[:index] + string[index + 2 :]
            index = 0
        else:
            index += 1
    return True