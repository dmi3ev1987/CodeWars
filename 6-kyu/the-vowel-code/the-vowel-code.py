PATTERN = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5',
    '1': 'a',
    '2': 'e',
    '3': 'i',
    '4': 'o',
    '5': 'u',
}
​
def encode(input_string):
    return ''.join(
        PATTERN[letter]
        if letter in PATTERN
        else letter
        for letter in input_string
    )
    
    
def decode(input_string):
    return encode(input_string)