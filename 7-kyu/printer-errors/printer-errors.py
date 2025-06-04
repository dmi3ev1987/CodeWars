def printer_error(input_string):
    return (
        f'{sum(letter > "m" for letter in input_string)}/{len(input_string)}'
    )
