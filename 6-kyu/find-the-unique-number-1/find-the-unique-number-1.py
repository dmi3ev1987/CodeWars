def find_uniq(arr):
    common_number = (
        arr[0] if (arr[0] == arr[1] or arr[0] == arr[2]) else arr[1]
    )
    for number in arr:
        if number != common_number:
            return number
​