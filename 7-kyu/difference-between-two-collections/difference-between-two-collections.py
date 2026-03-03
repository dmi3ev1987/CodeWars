def diff(a, b):
    result = set(a).difference(set(b)).union(set(b).difference(set(a)))
    return sorted(result)