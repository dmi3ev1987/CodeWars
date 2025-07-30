def multiplication_table(size):
    return [
        [
            inner_number
            for inner_number in range(number, (number * size) + 1, number)
        ]
        for number in range(1, size + 1)
    ]