def remove_parentheses(input_string):
    result = ''
    stack = []
    for index, char in enumerate(input_string):
        if char == '(':
            stack.append(char)
        if char == ')':
            stack.pop()
            continue
        if stack:
            continue
        result += char
    return result