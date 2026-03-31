def get_score(arr) -> int:
    lvl = 0
    lines_count = 0
    total_score = 0
    points_system = [40, 100, 300, 1200]
    
    for line in arr:
        if line > 0:
            total_score += points_system[line - 1] * (lvl + 1)
        lines_count += line
        if lines_count > 9:
            lvl += 1
            lines_count %= 10
​
    return total_score