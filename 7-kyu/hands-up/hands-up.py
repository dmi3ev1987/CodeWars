def get_positions(n):
    p_1 = n % 3
    p_2 = (n // 3) % 3
    p_3 = (n // 9) % 3
    return (p_1, p_2, p_3)
