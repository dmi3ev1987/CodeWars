def sort_cards(cards):
    pattern = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    return sorted(cards, key=pattern.index)