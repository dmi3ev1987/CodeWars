def perimeter(n):
    a, b = 0, 1
    total = a + b
    for _ in range(n):
        a, b = b, a + b
        total += b
    return total * 4