def double_every_other(input_list):
    return [
        number * 2 if index % 2 != 0 else number
        for index, number in enumerate(input_list)
    ]
