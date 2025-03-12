def persistence(n):
    count = 0
    if len(str(n)) == 1:
        return count
    while len(str(n)) > 1:
        digits_list = get_digits(n)
        n = multiply_result(digits_list)
        count += 1
    return count


def get_digits(digits_list):
    return [int(digit) for digit in str(digits_list)]


def multiply_result(input_list):
    result = 1
    for item in input_list:
        result *= item
    return result
