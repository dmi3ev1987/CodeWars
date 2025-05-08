def duplicate_count(text):
    text = text.lower()
    result_list = [item for item in text if text.count(item) > 1]
    return len(set(result_list))
