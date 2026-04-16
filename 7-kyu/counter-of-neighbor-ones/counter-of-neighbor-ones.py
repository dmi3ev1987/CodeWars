def ones_counter(arr):
    count = 0
    result = []
    for number in arr:
        if number == 0 and count != 0:
            result.append(count)
            count = 0
        else:
            count += number
    if count != 0:
        result.append(count)
    return result
