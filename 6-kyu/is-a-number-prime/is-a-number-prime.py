def is_prime(number):
    if number < 2:
        return False
    for current_number in range(2, int(number**0.5) + 1):
        if number % current_number == 0:
            return False
    return True
