def get_socks(name, socks):
    if len(socks) < 2:
        return []
    result = []
    current_color = socks[0]
    if name == 'Punky':
        for color in socks[1:]:
            if color != current_color:
                return [current_color, color]
    else:
        from collections import Counter
        counter = Counter(socks)
        for item, value in counter.items():
            if value >= 2:
                return [item] * 2
    return []