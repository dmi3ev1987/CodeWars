import random
​
​
def get_guess(input_number):
    random.randint = lambda a, b: input_number
    return input_number
​
​
guess = get_guess(55)