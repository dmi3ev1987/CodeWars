def is_very_even_number(input_number):
    total_sum = 0
    while input_number > 0:
        last_digit = input_number % 10
        total_sum += last_digit
        input_number //= 10
    if total_sum > 9:
        return is_very_even_number(total_sum)
    elif total_sum % 2 == 0:
        return True
    else:
        return False
