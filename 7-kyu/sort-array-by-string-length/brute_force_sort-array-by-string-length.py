def sort_by_length(input_array):
    result_dict = {}
    for word in input_array:
        result_dict[len(word)] = word
    return [result_dict[key] for key in sorted(result_dict.keys())]
