def nb_year(start_population, percent, addition_population, target_population):
    year_count = 0
    while start_population < target_population:
        start_population += int(
            start_population * percent / 100 + addition_population
        )
        year_count += 1
    return year_count
