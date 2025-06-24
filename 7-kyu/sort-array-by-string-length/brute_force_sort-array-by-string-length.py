def sort_by_length(input_array):
    words_dict = {len(word): word for word in input_array}
    return [words_dict[key] for key in sorted(words_dict.keys())]
