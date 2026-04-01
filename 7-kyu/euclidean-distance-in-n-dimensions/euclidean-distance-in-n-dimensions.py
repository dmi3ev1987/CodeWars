import math


def euclidean_distance(point1, point2):
    sum_squared = 0
    for i in range(len(point1)):
        sum_squared += (point1[i] - point2[i]) ** 2

    distance = math.sqrt(sum_squared)
    return round(distance, 2)
