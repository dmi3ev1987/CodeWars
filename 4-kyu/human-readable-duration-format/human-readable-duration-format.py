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
        text = f'{duration[item]} {text_item},'
        result.append(text)
    
    if len(result) > 1:
        result[-2] = result[-2][:-1]
        result[-1] = f'and {result[-1][:-1]}'
    elif len(result) == 1:
        result[0] = result[0][:-1]
        
    return ' '.join(result)