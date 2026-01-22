from collections import defaultdict


def order_food(developers):
    food = defaultdict(int)
    for developer in developers:
        food[developer['meal']] += 1
    return food
