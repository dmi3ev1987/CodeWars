SYMBOLS = {
    'units': {1: 'I', 4: 'IV', 5: 'V', 9: 'IX'},
    'tens': {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'},
    'hundreds': {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'},
    'thousands': {1: 'M'},
}
​
​
def solution(number):
    result = ''
​
    if not number or number < 1 or number > 3999:
        return result
​
    thousands = number // 1000
    if thousands:
        result += SYMBOLS['thousands'][1] * thousands
​
    hundreds = (number % 1000) // 100
    if hundreds:
        if hundreds in SYMBOLS['hundreds']:
            result += SYMBOLS['hundreds'][hundreds]
        elif hundreds < 4:
            result += SYMBOLS['hundreds'][1] * hundreds
        else:
            result += SYMBOLS['hundreds'][5] + SYMBOLS['hundreds'][1] * (
                hundreds - 5
            )
​
    tens = (number % 100) // 10
    if tens:
        if tens in SYMBOLS['tens']:
            result += SYMBOLS['tens'][tens]
        elif tens < 4:
            result += SYMBOLS['tens'][1] * tens
        else:
            result += SYMBOLS['tens'][5] + SYMBOLS['tens'][1] * (tens - 5)
​
    units = number % 10
    if units:
        if units in SYMBOLS['units']:
            result += SYMBOLS['units'][units]
        elif units < 4:
            result += SYMBOLS['units'][1] * units
        else:
            result += SYMBOLS['units'][5] + SYMBOLS['units'][1] * (units - 5)
​
    return result
​