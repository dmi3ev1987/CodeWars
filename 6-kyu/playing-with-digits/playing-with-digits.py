def dig_pow(n, p):
    result = 0
    for number in str(n):
        result += int(number) ** p
        p += 1
    if result % n == 0:
        return result // n
    return -1
​