def create_phone_number(n):
    area_code = ''.join(map(str, n[:3]))
    first_part = ''.join(map(str, n[3:6]))
    second_part = ''.join(map(str, n[6:]))
    return f'({area_code}) {first_part}-{second_part}'
​