def ones_counter(arr):
    count = 0
    result = []
    for number in arr:
        if number == 0:
            result.append(count)
            count = 0
        else:
            count += number
    result.append(count)
    return [num for num in result if num != 0]