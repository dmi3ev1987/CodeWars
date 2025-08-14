VOWELS = 'aeiou'
CIPHER = '12345'
​
def encode(input_string):
    return input_string.translate(str.maketrans(VOWELS, CIPHER))
    
    
def decode(input_string):
    return input_string.translate(str.maketrans(CIPHER, VOWELS))