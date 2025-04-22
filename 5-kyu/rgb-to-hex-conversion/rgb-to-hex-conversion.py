def rgb(r, g, b):
    r = check_out_of_range(r)
    g = check_out_of_range(g)
    b = check_out_of_range(b)
    return f'{r:02X}{g:02X}{b:02X}'
​
​
def check_out_of_range(number):
    return max(0, min(255, number))
​