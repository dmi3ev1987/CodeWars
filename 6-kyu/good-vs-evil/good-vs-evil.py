def good_vs_evil(good, evil):
    race_force_good = [1, 2, 3, 3, 4, 10]
    race_force_evil = [1, 2, 2, 2, 3, 5, 10]
    sum_good = 0
    sum_evil = 0
    for index, unit in enumerate(good.split()):
        sum_good += int(unit) * race_force_good[index]
    for index, unit in enumerate(evil.split()):
        sum_evil += int(unit) * race_force_evil[index]
    if sum_good == sum_evil:
        return 'Battle Result: No victor on this battle field'
    if sum_good > sum_evil:
        return 'Battle Result: Good triumphs over Evil'
    return 'Battle Result: Evil eradicates all trace of Good'