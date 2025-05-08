def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    for index in range(n - 3):
        signature.append(
            signature[index] + signature[index + 1] + signature[index + 2]
        )
    return signature
​