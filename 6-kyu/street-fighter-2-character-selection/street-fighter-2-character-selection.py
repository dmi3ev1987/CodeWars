def street_fighter_selection(fighters, initial_position, moves):
    opts = ['up', 'down', 'right', 'left']
    level, position = initial_position
    result = []

    for move in moves:
        if move == opts[0]:
            level = 0
        if move == opts[1]:
            level = 1
        if move == opts[2]:
            position = (position + 1) % len(fighters[0])
        if move == opts[3]:
            position = (position - 1) % len(fighters[0])
        result.append(fighters[level][position])
    return result
