def xbonacci(signature, n):
    start_position = 0
    while len(signature) < n:
        signature.append(sum(signature[start_position:]))
        start_position += 1
    return signature[:n]
