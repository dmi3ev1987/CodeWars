def divisors(integer):
    result = [number for number in range(2, integer) if integer % number == 0]
    return result if result else f'{integer} is prime'
