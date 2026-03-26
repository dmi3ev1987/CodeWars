def red_knight(v_pos, pown):
    knight = 0
    while knight != pown:
        pown += 1
        knight += 2
        v_pos = 1 if v_pos == 0 else 0
    color = 'White' if v_pos == 0 else 'Black'
    return (color, knight)
