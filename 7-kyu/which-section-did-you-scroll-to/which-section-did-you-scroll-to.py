def get_section_id(scroll, sizes):
    result = -1
    index = -1
    for size in sizes:
        result += size
        index += 1
        if result >= scroll:
            break
    return -1 if result < scroll else index
