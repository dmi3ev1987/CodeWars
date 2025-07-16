def longest_consec(strarr, k):
    if not strarr or k <= 0 or k > len(strarr):
        return ''

    max_length = 0
    result = ''

    for i in range(len(strarr) - k + 1):
        current = ''.join(strarr[i : i + k])
        if len(current) > max_length:
            max_length = len(current)
            result = current

    return result
