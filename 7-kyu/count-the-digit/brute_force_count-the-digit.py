def nb_dig(number, digit):
    count = 0
    for number in range(number + 1):
        count += str(number * number).count(str(digit))
    return count
