def abundant_number(num):
    devisors = []
    for current_num in range(1, num):
        if num % current_num == 0:
            devisors.append(current_num)
    return sum(devisors) > num
