def two_sum(numbers, target):
    result = None
    length = len(numbers)
    for index in range(length):
        for inner_index in range(length):
            if index == inner_index:
                continue
            if numbers[index] + numbers[inner_index] == target:
                result = (index, inner_index)
    return result
