def parts_sums(input_list):
    total = sum(input_list)
    result = [total]
    for number in input_list:
        total -= number
        result.append(total)
    return result
​