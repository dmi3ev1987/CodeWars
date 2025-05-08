    duration = {
        'years': years,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    }
    result = []
    for item in duration:
        if duration[item] == 0:
            continue
        if duration[item] == 1:
            text_item = item[:-1]
        else:
            text_item = item
        text = f'{duration[item]} {text_item}'
        result.append(text)
​
    return (
        ', '.join(result[:-1]) + ' and ' + result[-1]
        if len(result) > 1
        else result[0]
    )
​