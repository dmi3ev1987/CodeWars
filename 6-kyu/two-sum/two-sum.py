def two_sum(numbers, target):
    length = len(numbers)
    for index in range(length):
        for inner_index in range(length):
            if index == inner_index:
                continue
            if numbers[index] + numbers[inner_index] == target:
                return index, inner_index
    return None