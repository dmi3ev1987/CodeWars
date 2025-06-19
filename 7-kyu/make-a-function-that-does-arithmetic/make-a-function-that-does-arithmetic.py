import operator


def arithmetic(a, b, input_operator):
    operators = {
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': operator.mul,
        'divide': operator.truediv,
    }
    if input_operator in operators:
        return operators[input_operator](a, b)
    return None
