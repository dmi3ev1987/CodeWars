def nth_fib(n):
    fibo = [0, 1]
    if n < 3:
        return fibo[n - 1]
    for index in range(1, n - 1):
        fibo.append(fibo[index - 1] + fibo[index])
    return fibo[-1]
