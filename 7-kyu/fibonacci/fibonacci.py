def fibonacci(fibo_number: int) -> int:
    sequence = [0, 1, 1]
    if fibo_number > 2:
        for _ in range(2, fibo_number):
            sequence.append(sequence[-1] + sequence[-2])
    return sequence[fibo_number]
