def solution(s):
    letters_list = list(s)
    result_list = []
    for index in range(0, len(s), 2):
        try:
            result_list.append(letters_list[index] + letters_list[index + 1])
        except IndexError:
            result_list.append(letters_list[index] + "_")
    return result_list
​