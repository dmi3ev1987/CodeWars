def get_ages(age_sum, difference):
    if age_sum < 0 or difference < 0 or difference > age_sum:
        return None
    oldest = youngest = age_sum / 2
    while oldest - youngest < difference:
        oldest += 0.5
        youngest -= 0.5
    return oldest, youngest