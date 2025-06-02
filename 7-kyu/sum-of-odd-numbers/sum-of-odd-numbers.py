def row_sum_odd_numbers(n):
    # The first number in the nth row is n² - n + 1
    first_number = n * n - n + 1
    # The last number in the nth row is n² + n - 1
    last_number = n * n + n - 1
    # Sum of consecutive odd numbers from a to b is ((b - a) // 2 + 1) * (a + b) // 2
    return (
        ((last_number - first_number) // 2 + 1)
        * (first_number + last_number)
        // 2
    )
