def count_smileys(input_array):
    """Count valid smiley faces in an array.

    Valid smileys must have:
    - Exactly 1 eye (':' or ';')
    - Exactly 1 mouth (')' or 'D')
    - 0 or 1 nose ('-' or '~')
    - All characters must be in allowed set

    Args:
        input_array: List of strings to check

    Returns:
        Count of valid smiley faces
    """
    EYES = {':', ';'}
    MOUTHS = {')', 'D'}
    NOSES = {'-', '~'}
    ALLOWED = EYES | MOUTHS | NOSES  # Union of all valid characters

    count = 0
    for face in input_array:
        # Count components
        eye_count = sum(c in EYES for c in face)
        mouth_count = sum(c in MOUTHS for c in face)
        nose_count = sum(c in NOSES for c in face)

        # Check all conditions
        if (
            eye_count == 1
            and mouth_count == 1
            and nose_count <= 1
            and all(c in ALLOWED for c in face)
            and len(face) in (2, 3)
        ):  # Additional length check for efficiency
            count += 1

    return count
