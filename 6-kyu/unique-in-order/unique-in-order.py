def unique_in_order(sequence):
    result_list = []
    for item in sequence:
        if len(result_list) > 0:
            if item != result_list[-1]:
                result_list.append(item)
        else:
            result_list.append(item)
    return result_list
​