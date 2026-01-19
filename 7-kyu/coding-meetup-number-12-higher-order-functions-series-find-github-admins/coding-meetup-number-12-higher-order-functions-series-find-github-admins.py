def find_admin(developers, language):
    return [
        developer
        for developer in developers
        if developer['language'] == language
        and developer['githubAdmin'] == 'yes'
    ]
