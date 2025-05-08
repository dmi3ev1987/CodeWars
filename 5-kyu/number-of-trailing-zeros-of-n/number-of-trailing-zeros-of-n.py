def zeros(n):
    count_zeros = 0
    k = 5
    while n // k > 0:
        count_zeros += n // k
        k *= 5
    return count_zeros
