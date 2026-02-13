def sum_nested(input_list):
    total = 0
    while input_list:
        value = input_list.pop()
        if isinstance(value, int):
            total += value
        else:
            for part in value:
                input_list.append(part)
    return total