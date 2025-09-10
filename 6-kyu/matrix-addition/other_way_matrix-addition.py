def matrix_addition(matrix_a, matrix_b):
    for row in range(len(matrix_a)):
        for index in range(len(matrix_a[row])):
            matrix_a[row][index] += matrix_b[row][index]
    return matrix_a
