def encrypt_this(text):
    return ' '.join(
        str(ord(word[:1])) + word[-1] + word[2:-1] + word[1]
        if len(word) > 2
        else str(ord(word[:1])) + word[1:]
        for word in text.split()
    )