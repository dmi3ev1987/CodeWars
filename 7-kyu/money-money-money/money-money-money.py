def calculate_years(principal, interest, tax, desired):
    years_count = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        years_count += 1
    return years_count
