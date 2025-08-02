def diamond(size):
    if size <= 0 or size % 2 == 0:
        return None
    diamond_part = [
       ' ' * ((size - diamond) // 2) + '*' * diamond + '\n'
        for diamond in range(1, size + 1, 2)
    ]
    return ''.join(diamond_part + diamond_part[-2::-1])