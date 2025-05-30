def longest(string_a, string_b):
    return ''.join(sorted(set(string_a).union(set(string_b))))
