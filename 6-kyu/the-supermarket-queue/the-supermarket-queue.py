def queue_time(customers, checkout_tills_number):
    if checkout_tills_number == 1:
        return sum(customers)
    if checkout_tills_number >= len(customers):
        return max(customers)

    tills = [0] * checkout_tills_number
    for customer in customers:
        min_till = tills.index(min(tills))
        tills[min_till] += customer
    return max(tills)
