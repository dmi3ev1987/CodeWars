def permutations(input_string):
    if len(input_string) == 1:
        return input_string
    
    result = []
​
    for index in range(len(input_string)):
        first_letter = input_string[index]
        remaining_string = input_string[:index] + input_string[index+1:]
        for permutation in permutations(remaining_string):
            result.append(first_letter + permutation)
​
    return sorted(set(result))