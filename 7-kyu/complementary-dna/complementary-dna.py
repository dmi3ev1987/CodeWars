def DNA_strand(dna):
    DNA = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    return ''.join(
        DNA[unit] for unit in dna
    )