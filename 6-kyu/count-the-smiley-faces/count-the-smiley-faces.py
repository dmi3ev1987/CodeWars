def count_smileys(input_array):
    allowed_smile = {':', ';', '-', '~', ')', 'D'}
    eyes = {':', ';'}
    smiles = {')', 'D'}
    noses = {'-', '~'}
    return sum(
        sum(part in eyes for part in smile) == 1
        and sum(part in smiles for part in smile) == 1
        and sum(part in noses for part in smile) <= 1
        and all(part in allowed_smile for part in smile)
        for smile in input_array
    )