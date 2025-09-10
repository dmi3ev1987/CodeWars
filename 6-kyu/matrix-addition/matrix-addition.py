def matrix_addition(matrix_a, matrix_b):
    return [
        [
            matrix_a[index][inner_index] + matrix_b[index][inner_index]
            for inner_index in range(len(matrix_a[index]))
        ]
        for index in range(len(matrix_a))
    ]
