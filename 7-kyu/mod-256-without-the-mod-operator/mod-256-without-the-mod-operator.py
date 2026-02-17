def mod256_without_mod(input_number):
    mod_number = 256
    if abs(input_number) == mod_number:
        return 0
    if input_number > mod_number:
        result = int(input_number / mod_number)
        return input_number - (mod_number * result)
    elif input_number < 0:
        if -input_number < mod_number:
            return input_number + mod_number
        else:
            return (
                input_number
                - (int(input_number / mod_number)) * mod_number
                + mod_number
            )
    else:
        return input_number