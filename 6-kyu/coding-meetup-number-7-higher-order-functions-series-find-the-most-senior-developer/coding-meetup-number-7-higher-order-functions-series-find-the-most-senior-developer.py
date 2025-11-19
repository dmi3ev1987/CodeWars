def find_senior(input_list):
    input_list.sort(key=lambda x: x['age'], reverse=True)
    max_age = input_list[0]['age']
    count = 0
    for developer in input_list:
        if developer['age'] == max_age:
            count += 1
        else:
            break
    return input_list[:count]
