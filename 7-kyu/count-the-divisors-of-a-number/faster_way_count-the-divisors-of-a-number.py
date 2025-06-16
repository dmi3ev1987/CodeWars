def divisors(number):
    count = 0
    for current_number in range(1, int(number / 2) + 1):
        if number % current_number == 0:
            count += 1
    return count + 1
