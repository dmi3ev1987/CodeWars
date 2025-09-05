def validate(input_number):
    length = len(str(input_number))
    str_number = str(input_number)[::-1]
​
    result = []
    for index in range(length):
        current_number = int(str_number[index])
        if index % 2 == 1:
            doubled_number = current_number * 2
            result.append(doubled_number - 9 if doubled_number > 9 else doubled_number)
        else:
            result.append(current_number)
    return sum(result) % 10 == 0