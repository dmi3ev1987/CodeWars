def minimum_perimeter(area):
    min_per = 2 * (1 + area)
    for width in range(1, int(area**0.5) + 1):
        if area % width == 0:
            height = area // width
            min_per = min(min_per, 2 * (width + height))
    return min_per
