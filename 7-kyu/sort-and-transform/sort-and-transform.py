def sort_transform(arr):
    word_1 = [chr(num) for num in arr[:2] + arr[-2:]]
    arr_2 = sorted(arr)
    word_2 = [chr(num) for num in arr_2[:2] + arr_2[-2:]]
    result = [word_1, word_2, word_2[::-1], word_2]
    return '-'.join(''.join(word) for word in result)