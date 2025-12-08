def greet_developers(input_list):
    for developer in input_list:
        developer['greeting'] = (
            f'Hi {developer["firstName"]}, what do you like the most about {developer["language"]}?'
        )
    return input_list