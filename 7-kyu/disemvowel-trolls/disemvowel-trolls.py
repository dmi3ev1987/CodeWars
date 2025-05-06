def disemvowel(string_):
    vowels = 'aeiou'
    word_list = string_.split(" ")
    new_list = []
    for word in word_list:
        new_word = [
            letter for letter in word if letter.lower() not in vowels 
        ]
        new_list.append(''.join(new_word))
    return ' '.join(new_list)