def to_weird_case(words):
    return ' '.join(
        ''.join(
            letter.lower() if index % 2 else letter.upper()
            for index, letter in enumerate(word)
        )
        for word in words.split()
    )