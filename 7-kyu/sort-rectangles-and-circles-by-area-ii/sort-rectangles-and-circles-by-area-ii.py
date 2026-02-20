from math import pi


def sort_by_area(sequence):
    return sorted(
        sequence, key=lambda x: x[0] * x[1] if type(x) == tuple else pi * x**2
    )
