def find_next_square(square):
    return int((square**0.5 + 1) ** 2) if (square**0.5).is_integer() else -1
