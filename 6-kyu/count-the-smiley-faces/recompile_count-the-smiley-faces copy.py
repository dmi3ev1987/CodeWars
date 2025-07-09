import re


def count_smileys(input_array):
    """Count valid smiley faces using regex.

    ^ - Starts with
    [:;] - Matches exactly one eye character (: or ;)
    [-~]? - Matches 0 or 1 nose character (- or ~) (? makes the preceding element optional)
    [)D] - Matches exactly one mouth character () or D)
    $ - Ends with
    """
    pattern = re.compile(r'^[:;][-~]?[)D]$')  # Compile once
    return sum(1 for smile in input_array if pattern.match(smile))
