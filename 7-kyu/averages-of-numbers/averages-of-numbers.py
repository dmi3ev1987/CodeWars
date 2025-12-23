def averages(input_array):
    return (
        [
            (input_array[index] + input_array[index + 1]) / 2
            for index in range(len(input_array) - 1)
        ]
        if input_array
        else []
    )
