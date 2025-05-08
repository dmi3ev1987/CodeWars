    years = seconds // coefficient
​
    seconds = seconds % coefficient
    coefficient = 60 * 60 * 24
    days = seconds // coefficient
​
    seconds = seconds % coefficient
    coefficient = 60 * 60
    hours = seconds // coefficient
​
    seconds = seconds % coefficient
    coefficient = 60
    minutes = seconds // coefficient
​
    seconds = seconds % coefficient
​
    return {
        'years': years,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    }
​