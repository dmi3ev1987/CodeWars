def sort_array(source_array):
    odds = sorted(number for number in source_array if number % 2)
    odd_index = 0
​
    for index in range(len(source_array)):
        if source_array[index] % 2:
            source_array[index] = odds[odd_index]
            odd_index += 1
    return source_array