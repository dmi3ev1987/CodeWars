def pendulum(values):
    sorted_values = sorted(values)
    return sorted_values[::2][::-1] + sorted_values[1::2]
