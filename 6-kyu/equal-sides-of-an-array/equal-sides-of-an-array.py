def find_even_index(array):
    for index in range(len(array)):
        if sum(array[:index]) == sum(array[index + 1 :]):
            return index
    return -1