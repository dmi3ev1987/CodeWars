def highest_value(a, b):
    worth_a = sum(ord(char) for char in a)
    worth_b = sum(ord(char) for char in b)
    return a if worth_a >= worth_b else b