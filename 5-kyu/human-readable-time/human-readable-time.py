def make_readable(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
