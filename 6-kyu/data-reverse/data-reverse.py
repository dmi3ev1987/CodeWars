def data_reverse(data):
    bits_number = 8
    reversed_lists = [
        data[index : index + bits_number]
        for index in range(0, len(data), bits_number)
    ][::-1]
    result = []
    for list in reversed_lists:
        result.extend(list)
    return result