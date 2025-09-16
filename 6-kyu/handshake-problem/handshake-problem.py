def get_participants(handshakes):
    people = 0
    current_handshakes = 0
    while handshakes > current_handshakes:
        people += 1
        current_handshakes += people - 1
    return people