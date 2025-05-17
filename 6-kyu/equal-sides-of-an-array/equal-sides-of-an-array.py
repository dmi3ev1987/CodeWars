def find_even_index(array):
    left = 0
    for index in range(len(array)):
        if index != 0:
            left = sum(array[:index])
        right = sum(array[index + 1 :])
        if left == right:
            return index
    return -1
