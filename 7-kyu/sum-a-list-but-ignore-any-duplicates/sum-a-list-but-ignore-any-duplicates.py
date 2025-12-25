from collections import Counter


def sum_no_duplicates(input_list):
    result = 0
    number_counts = Counter(input_list)
    for key, value in number_counts.items():
        if value == 1:
            result += key
    return result
