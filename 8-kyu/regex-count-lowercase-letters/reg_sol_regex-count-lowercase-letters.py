import re


def lowercase_count(input_string):
    return len(re.findall('[a-z]', input_string))
