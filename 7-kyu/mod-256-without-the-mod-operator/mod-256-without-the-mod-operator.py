def mod256_without_mod(input_number):
    mod_number = 256
    result = input_number
    while result >= mod_number:
        result -= mod_number
    while result < 0:
        result += mod_number
    return result
