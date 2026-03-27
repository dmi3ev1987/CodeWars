def fibs_fizz_buzz(n):
    a, b = 1, 1
    result = [a, b]
    for _ in range(n):
        a, b = a + b, a
        result.append(a)
        if result[-1] % 3 == 0 and result[-1] % 5 == 0:
            result[-1] = 'FizzBuzz'
        elif result[-1] % 3 == 0:
            result[-1] = 'Fizz'
        elif result[-1] % 5 == 0:
            result[-1] = 'Buzz'
    return result[:n]
