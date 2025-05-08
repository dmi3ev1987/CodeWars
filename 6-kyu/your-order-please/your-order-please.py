def order(sentence):
    sentence_list = sentence.split()
    result_list = []
    for index in range(1, len(sentence_list)+1):
        for word in sentence_list:
            if str(index) in word:
                result_list.append(word)
    return " ".join(result_list)
