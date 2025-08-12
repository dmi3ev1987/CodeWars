def rev_rot(input_sting: str, chunk_size: int) -> str:
    if not input_sting or chunk_size <= 0 or len(input_sting) < chunk_size:
        return ''
    return ''.join(
        chunk[1:] + chunk[0]
        if sum(int(digit) for digit in chunk) % 2
        else chunk[::-1]
        for chunk in [
            input_sting[index : index + chunk_size]
            for index in range(0, len(input_sting), chunk_size)
            if len(input_sting[index : index + chunk_size]) == chunk_size
        ]
    )
