def cakes(recipe, available):
    result = [
        available[key] // recipe[key] if key in available else 0
        for key in recipe
    ]
    return min(result)
