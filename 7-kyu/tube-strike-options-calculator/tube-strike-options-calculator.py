def calculator(distance, bus_drive, bus_walk):
    walk_time = distance / walk
    bus_time = bus_drive / bus + bus_walk / walk
    if walk_time > 2:
        return 'Bus'
    if walk_time < 10 / 60:
        return 'Walk'
    if walk_time <= bus_time:
        return 'Walk'
    else:
        return 'Bus'
​