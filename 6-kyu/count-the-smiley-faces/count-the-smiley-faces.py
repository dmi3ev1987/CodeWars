import re
​
​
def count_smileys(input_array):
    return sum(
        1 for smile in input_array if re.match(r'^[:;][-~]?[)D]$', smile)
    )