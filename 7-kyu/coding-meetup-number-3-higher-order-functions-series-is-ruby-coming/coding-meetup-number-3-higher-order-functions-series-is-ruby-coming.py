def is_ruby_coming(developers_list):
    return any(
        developer['language'] == 'Ruby' for developer in developers_list
    )
