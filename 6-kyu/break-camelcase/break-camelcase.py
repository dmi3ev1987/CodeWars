def solution(inner_string):
    return ''.join(
        ' ' + letter if letter.isupper() else letter for letter in inner_string
    )