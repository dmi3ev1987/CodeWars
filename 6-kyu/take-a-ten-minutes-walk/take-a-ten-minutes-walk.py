def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    direction_counts = {
        'n': walk.count('n'),
        's': walk.count('s'),
        'w': walk.count('w'),
        'e': walk.count('e'),
    }
    return (
        direction_counts['n'] == direction_counts['s']
        and direction_counts['w'] == direction_counts['e']
    )
​