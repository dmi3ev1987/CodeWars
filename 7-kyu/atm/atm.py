def solve(cash):
    if cash % 10 != 0:
        return -1
    count = 0
    while cash >= 500:
        cash -= 500
        count += 1
    while cash >= 200:
        cash -= 200
        count += 1
    while cash >= 100:
        cash -= 100
        count += 1
    while cash >= 50:
        cash -= 50
        count += 1
    while cash >= 20:
        cash -= 20
        count += 1
    while cash >= 10:
        cash -= 10
        count += 1
    return count