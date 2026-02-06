def matrix(input_array):
    result_matrix = []
    counter = 0
    for inner_array in input_array:
        number_to_add = 0 if inner_array[counter] < 0 else 1
        result_matrix.append(
            inner_array[:counter]
            + [number_to_add]
            + inner_array[counter + 1 :]
        )
        counter += 1
    return result_matrix
