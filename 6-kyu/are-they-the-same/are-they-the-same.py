def comp(array, square_array):
    if array == [] and square_array == []:
        return True
    if not array or not square_array:
        return False
    for number in array:
        if number * number not in square_array:
            return False
        else:
            square_array.pop(square_array.index(number*number))
    return True