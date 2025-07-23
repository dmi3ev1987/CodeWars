def sum_dig_pow(a, b):
    result = []
    for number in range(a, b + 1):
        if number < 10:
            result.append(number)
        else:
            current_sum_of_digits = 0
            count = 1
            for digit in str(number):
                current_sum_of_digits += int(digit) ** count
                count += 1
            if current_sum_of_digits == number:
                result.append(number)
    return result