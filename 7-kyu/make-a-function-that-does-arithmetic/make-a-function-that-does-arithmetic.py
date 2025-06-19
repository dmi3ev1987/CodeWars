def arithmetic(a, b, operator):
    operators = {
        'add': lambda: a + b,
        'subtract': lambda: a - b,
        'multiply': lambda: a * b,
        'divide': lambda: a / b,
    }
    if operator in operators:
        return operators[operator]()
    return None
