def prefill(size_number, value='undefined'):
    message = f'{size_number} is invalid'
    try:
        int_size_number = int(size_number)
    except (ValueError, TypeError):
        raise TypeError(message)
    if int_size_number < 0:
        raise TypeError(message)
    return int_size_number * [value]
