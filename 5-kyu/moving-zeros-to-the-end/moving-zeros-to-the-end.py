def move_zeros(lst):
    result_lst = [item for item in lst if item != 0]
    return result_lst + [0] * (len(lst) - len(result_lst))
​