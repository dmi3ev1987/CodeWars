def high_and_low(numbers):
    numbers = [int(number) for number in numbers.split(' ')]
    return f'{max(numbers)} {min(numbers)}'