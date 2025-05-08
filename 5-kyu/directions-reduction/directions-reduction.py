def dir_reduc(arr):
    dir_dict = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST',
    }
    index = 0
    while index < len(arr) - 1:
        if arr[index + 1] == dir_dict[arr[index]]:
            arr.pop(index)
            arr.pop(index)
            if index > 0:
                index -= 1
        else:
            index += 1
    return arr
