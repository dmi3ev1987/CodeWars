def count_deaf_rats(town):
    town = town.replace(' ', '')
    coax_list = town.split('P')
    coax = list(coax_list[0][::-1] + coax_list[1])
    deaf_count = 0
    while coax:
        if coax[0] == '~':
            deaf_count += 1
        coax.pop(0)
        coax.pop(0)
    return deaf_count
