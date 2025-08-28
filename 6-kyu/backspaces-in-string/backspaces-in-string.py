def clean_string(input_string):
    stack = []
    backspace = '#'
    for letter in input_string:
        if letter == backspace:
            if stack:
                stack.pop()
        else:
            stack.append(letter)
    return ''.join(stack)
