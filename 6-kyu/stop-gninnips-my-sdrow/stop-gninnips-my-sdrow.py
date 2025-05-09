def spin_words(sentence):
    words_list = sentence.split()
    result_sentence_list = [
        word[::-1] if len(word) >= 5 else word for word in words_list
    ]
    return ' '.join(result_sentence_list)
