from preloaded import NATO  # NATO['A'] == 'Alfa', etc


def to_nato(words: str) -> str:
    return ' '.join(
        NATO[letter.upper()]
        if letter.isalpha()
        else ('' if letter == ' ' else letter)
        for letter in words.strip()
    ).replace('  ', ' ')
