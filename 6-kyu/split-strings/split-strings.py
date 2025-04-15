def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    return [s[index:index + 2] for index in range(0, len(s), 2)]
​