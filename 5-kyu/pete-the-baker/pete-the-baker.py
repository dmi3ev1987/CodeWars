def cakes(recipe, available):
    result = [
        available[key] // recipe[key] if key in available.keys() else 0
        for key in recipe.keys()
    ]
    return min(result)
