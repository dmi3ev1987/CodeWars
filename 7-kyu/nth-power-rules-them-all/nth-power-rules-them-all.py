def modified_sum(input_array, increase_power):
    return sum(
        [number ** increase_power for number in input_array]
    ) - sum(input_array)