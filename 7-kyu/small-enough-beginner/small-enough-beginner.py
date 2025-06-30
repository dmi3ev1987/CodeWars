def small_enough(array, limit):
    return all(True if number <= limit else False for number in array)