def solution(roman: str) -> int:
    """Transform the roman numeral into an integer."""
    symbols = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }
    subtractive_symbols = {
        'CM': 900,
        'CD': 400,
        'XC': 90,
        'XL': 40,
        'IX': 9,
        'IV': 4,
    }
    result = 0
    for key in subtractive_symbols:
        if key in roman:
            roman = roman.replace(key, '')
            result += subtractive_symbols[key]
    for symbol in roman:
        if symbol in symbols:
            result += symbols[symbol]
    return result
