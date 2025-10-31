def power_of_two(x):
    count = 0
    result = 0
    while result < x:
        result = 2**count
        count += 1
    return result == x if x > 0 else False
