def is_same_language(developers):
    language = developers[0]['language']
    for developer in developers[1:]:
        if developer['language'] != language:
            return False
    return True
