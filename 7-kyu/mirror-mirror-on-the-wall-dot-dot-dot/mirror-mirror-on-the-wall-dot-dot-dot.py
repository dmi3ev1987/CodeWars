def mirror(input_list: list) -> list:
    sorted_list = sorted(input_list)
    return sorted_list + sorted_list[:-1][::-1]
