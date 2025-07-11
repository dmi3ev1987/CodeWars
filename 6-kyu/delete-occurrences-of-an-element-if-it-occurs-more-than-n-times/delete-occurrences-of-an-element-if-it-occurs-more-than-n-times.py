from collections import defaultdict
​
​
def delete_nth(order, max_e):
    number_counter = defaultdict(int)
    result = []
    for number in order:
        if number_counter[number] < max_e:
            result.append(number)
            number_counter[number] += 1
    return result