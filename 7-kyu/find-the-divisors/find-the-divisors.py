def divisors(integer):
    result = [number for number in range(2, integer) if integer % number == 0]
    if result:
        return result
    return f'{integer} is prime'
