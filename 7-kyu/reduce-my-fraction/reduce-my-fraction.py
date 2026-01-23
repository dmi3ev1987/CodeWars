def reduce_fraction(fraction):
    numerator, denominator = fraction
    # Euclidean algorithm for greatest common divisor (GCD)
    a, b = numerator, denominator
    while b:
        a, b = b, a % b
    gcd = a
    return numerator // gcd, denominator // gcd
