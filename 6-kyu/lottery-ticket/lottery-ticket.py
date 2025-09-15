def bingo(ticket, win):
    win_count = 0
    for mini_win in ticket:
        for letter in mini_win[0]:
            if ord(letter) == mini_win[1]:
                win_count += 1
                break
    return 'Winner!' if win_count >= win else 'Loser!'
