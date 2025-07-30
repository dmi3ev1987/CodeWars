def multiplication_table(size):
    return [
        [inner_number * number for inner_number in range(1, size + 1)]
        for number in range(1, size + 1)
    ]