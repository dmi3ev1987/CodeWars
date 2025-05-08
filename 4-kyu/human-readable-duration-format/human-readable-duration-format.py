def format_duration(seconds) -> str:
    if seconds == 0:
        return 'now'
    duration = get_duration_dict(seconds)

    result = [
        f'{duration[item]} {item[:-1] if duration[item] == 1 else item}'
        for item in duration
        if duration[item] != 0
    ]

    return (
        ', '.join(result[:-1]) + ' and ' + result[-1]
        if len(result) > 1
        else result[0]
    )


def get_duration_dict(seconds) -> dict:
    coefficient = 60 * 60 * 24 * 365
    years = seconds // coefficient

    seconds = seconds % coefficient
    coefficient = 60 * 60 * 24
    days = seconds // coefficient

    seconds = seconds % coefficient
    coefficient = 60 * 60
    hours = seconds // coefficient

    seconds = seconds % coefficient
