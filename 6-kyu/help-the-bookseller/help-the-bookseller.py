from collections import defaultdict
​
​
def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ''
    categories_dict = defaultdict(int)
    for categorie in stocklist:
        categories_dict[categorie[0]] += int(categorie.split()[-1])
    return ' - '.join(
        f'({categorie} : {categories_dict[categorie]})'
        for categorie in categories
    )