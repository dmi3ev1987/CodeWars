def one_punch(item):
    if item == '' or type(item) is not str:
        return 'Broken!'
    return ' '.join(
        word.replace('a', '')
        .replace('e', '')
        .replace('A', '')
        .replace('E', '')
        for word in sorted(item.split())
    )