def nb_dig(number, digit):
    return sum(str(number * number).count(str(digit)) for number in range(number + 1))