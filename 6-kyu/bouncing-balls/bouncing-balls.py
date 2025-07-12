def bouncing_ball(height, bounce, window):
    if height < 0 or bounce < 0 or bounce >= 1 or window >= height:
        return -1
    count = 0
    while height > window:
        height *= bounce
        count += 2
    return count - 1