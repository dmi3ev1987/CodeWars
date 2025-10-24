def fold_array(array, runs):
    if runs == 0:
        return array
    result_array = []
    length = len(array)
    for index in range(length // 2):
        result_array.append(array[index] + array[-(index + 1)])
    if length % 2:
        result_array.append(array[length // 2])
    return fold_array(result_array, runs - 1)