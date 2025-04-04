def count_bits(n):
    count = 0
    binary = to_binary(n)
    for bit in binary:
        if bit == "1":
            count += 1
    return count
​
​
def to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary += str(n % 2)
        n = n // 2
    return binary[::-1]
​