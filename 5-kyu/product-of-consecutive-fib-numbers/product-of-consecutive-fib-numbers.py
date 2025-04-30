def product_fib(_prod):
    fibo_numbers = [0, 1]
    count = 1
    result = 0
    while result <= _prod:
        f = fibo_numbers[count]
        f_previous = fibo_numbers[count - 1]
        fibo_numbers.append(f + f_previous)
        count += 1  
        result = f * f_previous 
    if result > _prod:
        count -= 2
        f = fibo_numbers[count]
        f_previous = fibo_numbers[count - 1]
        previous_result = f * f_previous
        if previous_result == _prod:
            return [f_previous, f, True]
    return [f, fibo_numbers[count+1], False]