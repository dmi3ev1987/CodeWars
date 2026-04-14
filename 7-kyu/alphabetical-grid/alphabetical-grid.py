def grid(n):
    if n < 0:
        return None
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            letter_code = ord('a') + ((i + j) % 26)
            row.append(chr(letter_code))
        result.append(' '.join(row))
    return '\n'.join(result)
