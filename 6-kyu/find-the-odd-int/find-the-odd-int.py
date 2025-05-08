def find_it(seq):
    result_dict = {}
    while len(seq) >= 1:
        number, count, new_seq = count_number(seq)
        result_dict[number] = count
        seq = new_seq
    return find_one_odd(result_dict)


def count_number(seq):
    number = seq[0]
    count = seq.count(number)
    result_seq = [item for item in seq if item != number]
    return number, count, result_seq


def find_one_odd(input_dict):
    return next(
        (key for key, value in input_dict.items() if value % 2 != 0),
        None,
    )
