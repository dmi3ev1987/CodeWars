def count_consonants(input_string):
    vowels = 'aeiou'
    consonants = ''
    for letter in input_string.lower():
        if (
            letter.isalpha()
            and letter not in vowels
            and letter not in consonants
        ):
            consonants += letter
    return len(consonants)
