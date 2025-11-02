def count_developers(input_list):
    count = 0
    for developer in input_list:
        if (
            developer['continent'] == 'Europe'
            and developer['language'] == 'JavaScript'
        ):
            count += 1
    return count