def maskify(card_number):
    if len(str(card_number)) > 4:
        return '#' * (len(str(card_number)) - 4) + str(card_number)[-4:]
    return card_number