def triple_double(num1, num2):
    current_char_1 = str(num1)[0]
    triple_count = 1
    for char_1 in str(num1)[1:]:
        if char_1 == current_char_1:
            triple_count += 1
        else:
            current_char_1 = char_1
            triple_count = 1

        if triple_count >= 3:
            for index in range(len(str(num2)) - 1):
                if str(num2)[index] == str(num2)[index + 1] == current_char_1:
                    return True
    return False
