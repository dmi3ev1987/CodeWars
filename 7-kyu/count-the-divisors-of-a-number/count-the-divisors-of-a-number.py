def divisors(number):
    count = 0
    for current_number in range(1, number + 1):
        if number % current_number == 0:
            count += 1
    return count
