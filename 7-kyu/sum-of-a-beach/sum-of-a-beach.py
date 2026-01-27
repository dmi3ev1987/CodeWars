def sum_of_a_beach(beach):
    beach = beach.lower()
    counter = 0
    for word in ['sand', 'water', 'fish', 'sun']:
        while word in beach:
            counter += 1
            beach = beach.replace(word, '', 1)
    return counter
