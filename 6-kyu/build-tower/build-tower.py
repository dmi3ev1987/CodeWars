def tower_builder(n_floors):
    return [
        ((floor_number * 2 - 1) * '*').center(n_floors * 2 - 1)
        for floor_number in range(1, n_floors + 1)
    ]