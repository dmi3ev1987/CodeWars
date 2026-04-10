from math import gcd


def relatively_prime(n, lst):
    return [number for number in lst if gcd(n, number) == 1]
