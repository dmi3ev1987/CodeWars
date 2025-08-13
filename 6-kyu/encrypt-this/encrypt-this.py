def encrypt_this(text):
    encrypted_words = []
    for word in text.split():
        if not word:  # handle empty strings if any
            continue
            
        first_char = word[0]
        encrypted = str(ord(first_char))
        
        if len(word) > 1:
            second_char = word[1]
            last_char = word[-1]
            
            if len(word) > 2:
                middle = word[2:-1]
                encrypted += last_char + middle + second_char
            else:
                encrypted += last_char
                
        encrypted_words.append(encrypted)
    return ' '.join(encrypted_words)