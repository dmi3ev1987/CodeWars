def increment_string(strng):
    if not strng:
        return '1'
    prefix = strng.rstrip('0123456789')
    number_part = strng[len(prefix) :]
​
    if not number_part:
        return strng + '1'
    incremented_number = str(int(number_part) + 1)
    incremented_number = incremented_number.zfill(len(number_part))
​
    return prefix + incremented_number
​