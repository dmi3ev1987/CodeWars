def zeros(n):
    count = 0
    k = 5
    while n // k > 0:
        count += n // k
        k *= 5
    return count