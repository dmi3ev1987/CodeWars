def prefill(size_number=0, value=None):
    try:
        return int(size_number) * [value]
    except (ValueError, TypeError):
        raise TypeError(f'{size_number} is invalid')
