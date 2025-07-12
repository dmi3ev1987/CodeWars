def bouncing_ball(height, bounce, window):
    if not 0 < bounce < 1:
        return - 1
    count = 0
    while height > window:
        height *= bounce
        count += 1
        if height > window:
            count += 1
    return count or -1