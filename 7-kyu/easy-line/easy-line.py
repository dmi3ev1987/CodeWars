def easyline(n):
    one = 1
    old_list = []
    new_list = []
    for i in range(n + 1):
        if i == 0:
            old_list.append(one)
            new_list = old_list
        if i == 1:
            old_list.append(one)
            new_list = old_list
        if i > 1:
            new_list = []
            new_list.append(one)
            while len(old_list) >= 2:
                first = old_list.pop(0)
                second = old_list[0]
                new_list.append(first + second)
            new_list.append(one)
            old_list = new_list
    result = calculate_result(new_list)
    return result
​
​
def calculate_result(list):
    result = 0
    for item in list:
        result += item**2
    return result
​