def factorial(n):
    if n == 0:
        return 1
    if n < 0 or n > 12:
        raise ValueError('n is incorect')
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result