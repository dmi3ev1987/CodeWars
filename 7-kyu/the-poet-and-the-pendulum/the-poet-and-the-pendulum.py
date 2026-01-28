def pendulum(values):
    rigth_part = []
    left_part = []
    sorted_values = sorted(values, reverse=True)
    while sorted_values:
        rigth_part.append(sorted_values.pop())
        if sorted_values:
            left_part.append(sorted_values.pop())
    return rigth_part[::-1] + left_part