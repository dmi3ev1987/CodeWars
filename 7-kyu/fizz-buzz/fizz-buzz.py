def fizzbuzz(n):
    result = []
    for number in range(1, n + 1, 1):
        str_to_append = ''
        if number % 3 == 0:
            str_to_append += 'Fizz'
        if number % 5 == 0:
            str_to_append += 'Buzz'
        if str_to_append != '':
            result.append(str_to_append)
        else:
            result.append(number)
    return result
