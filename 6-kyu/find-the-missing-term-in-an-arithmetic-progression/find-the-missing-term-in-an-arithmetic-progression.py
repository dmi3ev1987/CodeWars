def find_missing(sequence):
    constant_difference = min(sequence[1] - sequence[0], sequence[-1] - sequence[-2])
    missing_term = sequence[0]
    for number in sequence:
        if missing_term != number:
            return missing_term
        missing_term += constant_difference
    return None