def dont_give_me_five(start, end):
    return len([number for number in range(start, end + 1) if '5' not in str(number)])