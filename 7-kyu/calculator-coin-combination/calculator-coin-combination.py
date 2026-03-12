def coin_combo(cents):
    result = [0, 0, 0, 0]
    while cents >= 25:
        cents -= 25
        result[3] += 1
    while cents >= 10:
        cents -= 10
        result[2] += 1
    while cents >= 5:
        cents -= 5
        result[1] += 1
    while cents >= 1:
        cents -= 1
        result[0] += 1
    return result
