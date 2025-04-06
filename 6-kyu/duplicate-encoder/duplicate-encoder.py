def duplicate_encode(word):
    word = word.lower()
    resust_word = ["(" if word.count(letter) == 1 else ")" for letter in word]
    return "".join(resust_word)
​