BRACES = {
    '{': '}',
    '[': ']',
    '(': ')',
}


def valid_braces(string):
    stack = []
    for brace in string:
        if brace in BRACES:
            stack.append(brace)
        else:
            if not stack or BRACES[stack.pop()] != brace:
                return False
    return not stack
