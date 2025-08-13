def encrypt_this(text):
    result = []
    for word in text.split():
        if len(word) > 2:
            encrypted_word = str(ord(word[:1])) + word[-1] + word[2:-1]+ word[1]
        else:
            encrypted_word = str(ord(word[:1])) + word[1:]
        result.append(encrypted_word)
    return ' '.join(result)