def count_deaf_rats(town):
    town = town.replace(' ', '')
    coax_list = town.split('P')
    coax = list(coax_list[0] + coax_list[1][::-1])
    deaf_count = 0
    while coax:
        if coax[-1] == '~':
            deaf_count += 1
        coax.pop()
        coax.pop()
    return deaf_count