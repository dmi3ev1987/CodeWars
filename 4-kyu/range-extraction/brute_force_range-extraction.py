def solution(array):
    result = []
    while array:
        number_to_append = array.pop(0)
        if not array:
            result.append(str(number_to_append))
            break
        if number_to_append + 1 != array[0]:
            result.append(str(number_to_append))
        else:
            next_number = array[0] + 1
            for index in range(len(array)):
                if index != len(array) - 1 and array[index + 1] == next_number:
                    next_number = array[index + 1] + 1
                else:
                    if index >= 1:
                        result.append(f'{number_to_append}-{array[index]}')
                        array = array[index + 1 :]
                        break
                    result.append(str(number_to_append))
                    break

    return ','.join(result)
