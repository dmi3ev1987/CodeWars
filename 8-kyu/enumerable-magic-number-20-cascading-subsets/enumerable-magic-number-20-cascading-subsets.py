def each_cons(input_list, input_number):
    return [
        input_list[index : index + input_number]
        for index in range(len(input_list) - input_number + 1)
    ]
