def number(lines):
    count = 1
    result = []
    for line in lines:
        result.append(f'{count}: {line}')
        count += 1
    return result
