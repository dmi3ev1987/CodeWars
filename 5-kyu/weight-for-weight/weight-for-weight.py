def order_weight(strng):
    data = strng.split()
    for last_index in range(len(data)-1, 0, -1):
        swapped = False
        for item_index in range(last_index):
            value = sum(int(item) for item in data[item_index])
            value_next = sum(int(item) for item in data[item_index + 1])
            if value > value_next:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                swapped = True
            elif value == value_next and data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                swapped = True
        if not swapped:
            break
    return " ".join(data)