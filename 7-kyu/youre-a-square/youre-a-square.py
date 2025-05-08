def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    count = 1
    while count**2 <= n:
        if count**2 == n:
            return True
        if count**2 > n:
            return False
        count += 1
    return False
