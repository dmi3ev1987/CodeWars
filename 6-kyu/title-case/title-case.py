def title_case(title, minor_words=''):
    return ' '.join(
        word.lower()
        if word.lower() in minor_words.lower().split() and index != 0
        else word.capitalize()
        for index, word in enumerate(title.split())
    )
