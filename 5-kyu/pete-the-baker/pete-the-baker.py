def cakes(recipe, available):
    result = []
    for key in recipe.keys():
        if key not in available.keys():
            return 0
        result.append(
            available[key] // recipe [key] 
        )
    return min(result)