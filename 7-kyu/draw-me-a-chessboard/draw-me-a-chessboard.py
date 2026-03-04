def chess_board(rows, columns):
    cell_1 = 'O'
    cell_2 = 'X'
    board = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(cell_1)
            cell_1, cell_2 = cell_2, cell_1
        board.append(row)
        if columns % 2 == 0:
            cell_1, cell_2 = cell_2, cell_1
    return board
