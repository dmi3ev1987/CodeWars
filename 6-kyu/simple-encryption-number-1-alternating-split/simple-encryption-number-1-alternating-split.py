def decrypt(encrypted_text, n):
    if n <= 0 or not encrypted_text:
        return encrypted_text
    half = len(encrypted_text) // 2
    even_part = encrypted_text[:half]
    odd_part = encrypted_text[half:]
    text = []
    for index in range(half):
        text.append(odd_part[index])
        text.append(even_part[index])
    if len(odd_part) > half:
        text.append(odd_part[-1])
    text = ''.join(text)
    return decrypt(text, n - 1)
​
​
def encrypt(text, n):
    if n <= 0 or not text:
        return text
    even = []
    odd = []
    for index, letter in enumerate(text):
        if index % 2:
            even.append(letter)
        else:
            odd.append(letter)
    encrypted_text = ''.join(even + odd)
    return encrypt(encrypted_text, n - 1)