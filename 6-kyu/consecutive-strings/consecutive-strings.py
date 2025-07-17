def longest_consec(strings_array, consec_number):
    if (
        not strings_array
        or consec_number <= 0
        or consec_number > len(strings_array)
    ):
        return ''
​
    max_length = 0
    result = ''
​
    for i in range(len(strings_array) - consec_number + 1):
        current_string = ''.join(strings_array[i : i + consec_number])
        if len(current_string) > max_length:
            max_length = len(current_string)
            result = current_string
​
    return result