def get_participants(handshakes):
    participants = 0
    while handshakes > 0:
        handshakes -= participants
        participants += 1
    return participants
