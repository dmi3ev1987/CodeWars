from collections import Counter


def highest_rank(input_array):
    """Tuple (counter[x], x) as the sort key.

    - First sort by frequency (highest frequency first).
    - If frequencies are equal, sort by the key value (highest value first).
    """
    counter = Counter(input_array)
    return max(counter, key=lambda x: (counter[x], x))
