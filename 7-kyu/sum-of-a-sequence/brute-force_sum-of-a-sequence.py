def sequence_sum(begin_number, end_number, step):
    result = 0
    while begin_number <= end_number:
        result += begin_number
        begin_number += step
    return result
