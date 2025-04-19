def move_zeros(lst):
    result_lst = [item for item in lst if item != 0]
    zero_lst = [0 for item in range(lst.count(0))]
    return result_lst + zero_lst