def solution(number):
    natural_list = get_natural_list(number)
    result_list = []
    for item in natural_list:
        if item % 3 == 0 or item % 5 == 0:
            result_list.append(item)
    return get_sum_of_numbers(result_list)
​
​
def get_natural_list(number):
    return [item for item in range(number) if item != 0]
​
def get_sum_of_numbers(result_list):
    result = 0
    for item in result_list:
        result += item
    return result