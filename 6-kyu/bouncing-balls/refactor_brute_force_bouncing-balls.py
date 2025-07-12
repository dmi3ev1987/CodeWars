def bouncing_ball(height, bounce, window):
    if not (height > 0 and 0 < bounce < 1 and window < height):
        return -1

    bounces = 0
    while height > window:
        height *= bounce
        bounces += 1

    # The ball passes the window twice for each bounce (up and down),
    # except for the initial drop which is only once
    return bounces * 2 - 1 if bounces > 0 else -1
