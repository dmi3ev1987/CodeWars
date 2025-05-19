def solution(array):
    result = []
    start = next = array[0]
    for number in array[1:] + ['']:
        if number != next + 1:
            if next == start:
                result.append(str(start))
            elif next == start + 1:
                result.extend([str(start), str(next)])
            else:
                result.append(str(start) + '-' + str(next))
            start = number
        next = number
    return ','.join(result)