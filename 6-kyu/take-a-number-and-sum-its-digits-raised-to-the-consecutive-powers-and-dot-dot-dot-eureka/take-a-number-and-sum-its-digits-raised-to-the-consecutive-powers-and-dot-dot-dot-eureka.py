def sum_dig_pow(a, b):
    return [
        number
        for number in range(a, b + 1)
        if sum(
            int(digit) ** index for index, digit in enumerate(str(number), 1)
        )
        == number
    ]
