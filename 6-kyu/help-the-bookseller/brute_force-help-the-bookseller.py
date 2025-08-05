from collections import defaultdict


def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ''
    categories_dict = defaultdict(int)
    for categorie in stocklist:
        categories_dict[categorie[0]] += int(categorie.split()[-1])
    return ' - '.join(
        f'({categorie} : {categories_dict[categorie]})'
        if categorie in categories_dict
        else f'({categorie} : 0)'
        for categorie in categories
    )
