def dna_strand(dna):
    dna_units = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    return ''.join(dna_units[unit] for unit in dna)
