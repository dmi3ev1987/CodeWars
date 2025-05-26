def maskify(card_number):
    return '#' * (len(str(card_number)) - 4) + str(card_number)[-4:]