from math import pi


def sort_by_area(sequence):
    result = []
    index = 0
    squares = []
    for area in sequence:
        if type(area) == tuple:
            square = area[0] * area[1]
        else:
            square = pi * area**2
        squares.append((index, square))
        index += 1
    for sorted_area in sorted(squares, key=lambda x: x[1]):
        result.append(sequence[sorted_area[0]])
    return result
