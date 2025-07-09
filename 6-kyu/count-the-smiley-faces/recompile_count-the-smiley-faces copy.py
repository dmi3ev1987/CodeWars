import re


def count_smileys(input_array):
    """Count valid smiley faces using regex."""
    pattern = re.compile(r'^[:;][-~]?[)D]$')  # Compile once
    return sum(1 for face in input_array if pattern.match(face))
