def is_valid_IP(input_string):
    return (
        (
            sum(
                0 <= int(number) <= 255 and str(int(number)) == number
                for number in input_string.split('.')
                if number and all(digit.isdigit() for digit in number)
            )
            == 4
        )
        if input_string
        else False
    )