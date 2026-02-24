def sum_or_product(input_array, n):
    sorted_array = sorted(input_array)
    sum_n = sum(sorted_array[-n:])
    product = 1
    for number in sorted_array[:n]:
        product *= number
    if sum_n > product:
        return 'sum'
    if product > sum_n:
        return 'product'
    return 'same'