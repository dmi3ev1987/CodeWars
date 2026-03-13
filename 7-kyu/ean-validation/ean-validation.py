def validate_ean(code):
    code_sum = 0
    for index in range(12):
        if (index + 1) % 2 != 0:
            code_sum += int(code[index]) * 1
        else:
            code_sum += int(code[index]) * 3
    return str(10 - code_sum % 10)[-1] == code[-1]