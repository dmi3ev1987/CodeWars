def to_nato(words: str) -> str:
    nato_string = (
        'Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India '
        'Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo '
        'Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu'
    )
    nato_dict = {nato_word[0]: nato_word for nato_word in nato_string.split()}
    return ' '.join(
        nato_dict.get(char, char)
        for char in words.upper()
        if not char.isspace()
    )
