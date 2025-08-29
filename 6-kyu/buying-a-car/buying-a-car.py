def nb_months(
    start_price_old, start_price_new, saving_per_month, percent_loss_by_month
):
    count = 0
    savings = 0
    while start_price_old + savings < start_price_new:
        count += 1
        if count % 2 == 0:
            percent_loss_by_month += 0.5
        start_price_old = start_price_old * (100 - percent_loss_by_month) / 100
        start_price_new = start_price_new * (100 - percent_loss_by_month) / 100
        savings += saving_per_month
    return [count, round(start_price_old + savings - start_price_new)]