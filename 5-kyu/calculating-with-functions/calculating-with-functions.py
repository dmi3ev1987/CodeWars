​
​
def seven(calculation=None):
    return get_number_or_function(calculation, 7)
​
​
def eight(calculation=None):
    return get_number_or_function(calculation, 8)
​
​
def nine(calculation=None):
    return get_number_or_function(calculation, 9)
​
​
def plus(number):
    return lambda x: x + number
​
​
def minus(number):
    return lambda x: x - number
​
​
def times(number):
    return lambda x: x * number
​
​
def divided_by(number):
    return lambda x: int(x / number)