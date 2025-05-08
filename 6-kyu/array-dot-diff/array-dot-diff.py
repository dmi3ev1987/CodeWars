def array_diff(a, b):
    if not b:
        return a
    result_list = a
    for item_b in b:
        result_list = get_diff_list(result_list, item_b)
    return result_list


def get_diff_list(input_list, number):
    return [item for item in input_list if item != number]
