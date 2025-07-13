def find_nb(m):
    count = 0
    result = 0
    while result < m:
        count += 1
        result += count**3
    return count if result == m else -1
