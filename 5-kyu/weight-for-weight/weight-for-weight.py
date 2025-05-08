def order_weight(strng):
    data = strng.split()
    data.sort()
    data.sort(key=lambda number: sum(int(digit) for digit in number))
    return " ".join(data)
