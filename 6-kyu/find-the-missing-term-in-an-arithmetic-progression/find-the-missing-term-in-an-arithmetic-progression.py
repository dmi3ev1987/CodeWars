def find_missing(sequence):
    constant_difference = (sequence[-1] - sequence[0]) / len(sequence)
    missing_term = sequence[0]
    for number in sequence:
        if missing_term != number:
            return missing_term
        missing_term += constant_difference
    return None