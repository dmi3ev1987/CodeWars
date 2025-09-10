def matrix_addition(matrix_a, matrix_b):
    result = []
    for index in range(len(matrix_a)):
        matrix_part = []
        for inner_index in range(len(matrix_a[index])):
            matrix_part.append(
                matrix_a[index][inner_index] + matrix_b[index][inner_index]
            )
        result.append(matrix_part)
    return result
