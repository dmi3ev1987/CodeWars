def row_sum_odd_numbers(n):
    current_odd = 1
    result = []
    for index in range(1, n + 1):
        item = []
        for odd_number in range(index):
            item.append(current_odd)
            current_odd += 2
        result.append(item)

    return sum(result[-1])
