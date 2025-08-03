def sq_in_rect(length, width):
    if length == width:
        return None
    result = []
    squere_left = length * width
    while squere_left > 0:
        if width > length:
            width, length = length, width
        result.append(width)
        length -= width
        squere_left -= width ** 2
    return result