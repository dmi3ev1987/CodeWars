def increment_string(strng):
    zeros = number = 0
    incremeted_number = 1
    if not strng:
        return str(incremeted_number)
    for index in range(len(strng) - 1, -1, -1):
        if strng[index].isdigit():
            if index == 0:
                number = strng
                strng = ''
        else:
            number = strng[index + 1 :]
            strng = strng[: index + 1]
            break
    if number:
        incremeted_number = int(number) + 1
        if len(number) > len(str(incremeted_number)):
            zeros = len(number) - len(str(incremeted_number))
    incremeted_number = str(0) * zeros + str(incremeted_number)
    return strng + incremeted_number
​