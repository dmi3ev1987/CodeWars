def solve(input_string):
    chunks = []
    chunk = ''
    exception_letters = 'aeiou'
    for letter in input_string:
        if letter not in exception_letters:
            chunk += letter
        else:
            chunks.append(chunk)
            chunk = ''
    chunks.append(chunk)
    return max(
        sum(ord(letter) - ord('a') + 1 for letter in chunk) for chunk in chunks
    )