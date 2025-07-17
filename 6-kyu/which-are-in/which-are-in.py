def in_array(array1, array2):
    return sorted(
        {
            word
            for inner_word in array2
            for word in array1
            if word in inner_word
        }
    )