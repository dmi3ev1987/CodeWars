from collections import Counter


def odd_ones_out(numbers):
    counts = Counter(numbers)
    return [number for number in numbers if counts[number] % 2 == 0]
