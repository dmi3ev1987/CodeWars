def sort_by_language(arr):
    return sorted(arr, key=lambda arr: (arr['language'], arr['first_name']))