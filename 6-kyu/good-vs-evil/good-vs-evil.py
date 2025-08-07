def good_vs_evil(good, evil):
    race_force_good = [1, 2, 3, 3, 4, 10]
    race_force_evil = [1, 2, 2, 2, 3, 5, 10]
    sum_good = sum(
        int(unit) * race_force_good[index]
        for index, unit in enumerate(good.split())
    )
    sum_evil = sum(
        int(unit) * race_force_evil[index]
        for index, unit in enumerate(evil.split())
    )
    if sum_good == sum_evil:
        return 'Battle Result: No victor on this battle field'
    if sum_good > sum_evil:
        return 'Battle Result: Good triumphs over Evil'
    return 'Battle Result: Evil eradicates all trace of Good'