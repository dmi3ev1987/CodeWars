def solution(inner_string):
    result = []
    current_word = ''
    for letter in inner_string:
        current_word += letter
​
        if letter.isupper():
            result.append(current_word[:-1])
            current_word = letter
​
    result.append(current_word)
​
    return ' '.join(result)