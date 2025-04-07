def find_outlier(integers):
    even_list = []
    odd_list = []
    for number in integers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    if len(even_list) == 1:
        return even_list[0]
    return odd_list[0]
​