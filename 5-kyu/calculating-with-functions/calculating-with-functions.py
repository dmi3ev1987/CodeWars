def get_number_or_function(calculation, number):
    if calculation:
        return calculation(number)
    return number


def zero(calculation=None):
    return get_number_or_function(calculation, 0)


def one(calculation=None):
    return get_number_or_function(calculation, 1)


def two(calculation=None):
    return get_number_or_function(calculation, 2)


def three(calculation=None):
    return get_number_or_function(calculation, 3)


def four(calculation=None):
    return get_number_or_function(calculation, 4)


def five(calculation=None):
    return get_number_or_function(calculation, 5)


def six(calculation=None):
    return get_number_or_function(calculation, 6)


def seven(calculation=None):
    return get_number_or_function(calculation, 7)


def eight(calculation=None):
    return get_number_or_function(calculation, 8)


def nine(calculation=None):
    return get_number_or_function(calculation, 9)


def plus(number):
    return lambda x: x + number


def minus(number):
    return lambda x: x - number


def times(number):
    return lambda x: x * number


def divided_by(number):
    return lambda x: x // number
