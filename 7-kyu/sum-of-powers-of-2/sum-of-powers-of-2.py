def powers(input_number):
    power_of_two = [1]
    power = 1
    result = []
    while power_of_two[-1] < input_number:
        power_of_two.append(2 ** power)
        power += 1
    while input_number > 0:
        number = power_of_two.pop()
        if number <= input_number:
            result.append(number)
            input_number -= number
    return result[::-1]