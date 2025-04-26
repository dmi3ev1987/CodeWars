​
def six(calculation=None):
    return get_number_or_function(calculation, 6)
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
    def nested_function(x):
        return x + number
​
    return nested_function
​
​
def minus(number):
    def nested_function(x):
        return x - number
​
    return nested_function
​
​
def times(number):
    def nested_function(x):
        return x * number
​
    return nested_function
​
​
def divided_by(number):
    def nested_function(x):
        return int(x / number)
​
    return nested_function
​