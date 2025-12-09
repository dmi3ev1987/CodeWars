import math


def circle_area(radius):
    if radius <= 0:
        raise ValueError
    return math.pi * (radius**2)
