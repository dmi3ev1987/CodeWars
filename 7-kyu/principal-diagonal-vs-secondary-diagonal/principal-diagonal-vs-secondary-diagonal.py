def diagonal(matrix):
    principal_diagonal = 0
    secondary_diagonal = 0
    for row in range(len(matrix)):
        principal_diagonal += matrix[row][row]
        secondary_diagonal += matrix[row][-(row + 1)]
    print(principal_diagonal, secondary_diagonal)
    if principal_diagonal > secondary_diagonal:
        return 'Principal Diagonal win!'
    elif principal_diagonal < secondary_diagonal:
        return 'Secondary Diagonal win!'
    else:
        return 'Draw!'
