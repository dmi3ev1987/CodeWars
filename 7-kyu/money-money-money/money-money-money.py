def calculate_years(principal, interest, tax, desired):
    count = 0
    while principal < desired:
        income = principal * interest
        principal += income - income * tax
        count += 1
    return count
