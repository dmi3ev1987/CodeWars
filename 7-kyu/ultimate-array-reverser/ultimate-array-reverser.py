def reverse(input_array):
    reversed = ''.join(input_array)[::-1]
    result = []
    position = 0
    for item in input_array:
        length = len(item)
        result.append(reversed[position : position + length])
        position += length
    return result
