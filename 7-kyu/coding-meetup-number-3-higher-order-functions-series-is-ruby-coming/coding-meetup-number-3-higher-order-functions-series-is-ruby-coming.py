def is_ruby_coming(developers_list): 
    for developer in developers_list:
        if developer['language'] == 'Ruby':
            return True
    return False