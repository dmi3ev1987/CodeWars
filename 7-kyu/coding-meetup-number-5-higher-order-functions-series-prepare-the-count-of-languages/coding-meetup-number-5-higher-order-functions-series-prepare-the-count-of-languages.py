def count_languages(developers):
    language_count = {}
    for developer in developers:
        language = developer['language']
        language_count[language] = language_count.get(language, 0) + 1
    return language_count