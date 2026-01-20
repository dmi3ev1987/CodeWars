def get_average(developers):
    return round(
        sum(developer['age'] for developer in developers) / len(developers)
    )