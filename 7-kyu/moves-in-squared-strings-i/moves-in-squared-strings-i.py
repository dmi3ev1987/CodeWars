def vert_mirror(input_string):
    return '\n'.join([part[::-1] for part in input_string.split('\n')])
    
def hor_mirror(input_string):
    return '\n'.join(reversed(input_string.split('\n')))
    
def oper(input_function, input_string):
    return input_function(input_string)