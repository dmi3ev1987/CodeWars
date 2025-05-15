def get_middle(string):
    lenght = len(string)
    middle_index = lenght // 2
    if lenght % 2:
        return string[middle_index]
    return string[middle_index - 1 : middle_index + 1]
