def snail(snail_map):
    result = []
    start = 0
    stop = len(snail_map)
    while start < stop:
        result.extend(snail_map[start][start:stop])

        for index in range(start + 1, stop):
            result.append(snail_map[index][stop - 1])

        if start != stop - 1:
            result.extend(snail_map[stop - 1][start : stop - 1][::-1])

            for index in range(stop - 2, start, -1):
                result.append(snail_map[index][start])

        start += 1
        stop -= 1

    return result
