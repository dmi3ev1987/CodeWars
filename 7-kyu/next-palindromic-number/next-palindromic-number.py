def next_pal(input_number):
    while True:
        input_number += 1
        half_number_length = len(str(input_number)) // 2
        if (
            str(input_number)[:half_number_length]
            == str(input_number)[-half_number_length:][::-1]
        ):
            break
    return input_number
