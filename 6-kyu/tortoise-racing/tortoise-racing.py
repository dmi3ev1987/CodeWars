def race(speed_1, speed_2, gap):
    if speed_1 >= speed_2:
        return None
    hours = gap / (speed_2 - speed_1)
    minutes = (hours * 60) % 60
    seconds = (hours * 3600) % 60
    return [int(hours), int(minutes), int(seconds)]