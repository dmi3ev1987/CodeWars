def unique_in_order(sequence):
    result_list = []
    for item in sequence:
        if not result_list or item != result_list[-1]:
            result_list.append(item)
    return result_list
​