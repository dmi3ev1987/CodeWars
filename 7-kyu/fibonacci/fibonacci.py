def fibonacci(fibo_number: int) -> int:
    x, y = 0, 1
    for _ in range(fibo_number):
        x, y = y, x + y
    return x