def delete_nth(order, max_e):
    number_dict = {number: 0 for number in set(order)}
    result = []
    for number in order:
        if number_dict[number] < max_e:
            result.append(number)
            number_dict[number] += 1
    return result
