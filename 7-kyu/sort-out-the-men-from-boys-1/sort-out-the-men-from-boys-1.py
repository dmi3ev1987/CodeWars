def men_from_boys(input_array):
    mens = []
    boys = []
    for unit in set(input_array):
        if unit % 2 == 0:
            mens.append(unit)
        else:
            boys.append(unit)
    return sorted(mens) + sorted(boys, reverse=True)
