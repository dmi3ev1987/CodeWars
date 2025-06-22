def comp(array, square_array):
    if array is None or square_array is None:
        return False
    if not array and not square_array:
        return True
    return sorted(number * number for number in array) == sorted(square_array)
