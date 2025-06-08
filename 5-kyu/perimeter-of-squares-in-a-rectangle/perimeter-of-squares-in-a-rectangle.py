def perimeter(n):
    if n <= 0:
        return 4
    a, b = 1, 1
    total = a + b
    for _ in range(2, n + 1):
        a, b = b, a + b
        total += b
    return total * 4