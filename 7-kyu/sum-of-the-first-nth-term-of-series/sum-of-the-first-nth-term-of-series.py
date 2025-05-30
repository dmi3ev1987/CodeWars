def series_sum(n):
    result = 0
    temp_list = [1]
    if n > 1:
        for _ in range(1, n):
            temp_list.append(temp_list[-1] + 3)
        result = calc(temp_list)
    else:
        result = n
    return f'{result:.2f}'


def calc(list):
    result = 0
    for item in list:
        result += 1 / item
    return round(result, 2)
