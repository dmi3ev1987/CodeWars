def round_to_next5(number):
    return number if number % 5 == 0 else 5 * ((number // 5) + 1)
