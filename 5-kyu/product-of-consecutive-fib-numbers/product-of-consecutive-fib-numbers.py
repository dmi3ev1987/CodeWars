def product_fib(_prod):
    a, b = 0, 1
    while a * b < _prod:
        a, b = b, a + b
    return [a, b, a * b == _prod]
