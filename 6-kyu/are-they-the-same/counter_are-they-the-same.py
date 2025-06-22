from collections import Counter


def comp(array, square_array):
    if array is None or square_array is None:
        return False
    if not array and not square_array:
        return True
    return Counter(number * number for number in array) == Counter(
        square_array
    )
