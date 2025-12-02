def hotpo(input_number):
    count = 0
    while input_number != 1:
        if input_number % 2 == 0:
            input_number /= 2
        else:
            input_number = input_number * 3 + 1
        count += 1
    return count
