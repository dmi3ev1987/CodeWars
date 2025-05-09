def generate_hashtag(s):
    stripped = s.strip()
    if not stripped:
        return False
    hashtag = '#' + ''.join(word.capitalize() for word in stripped.split())
    if len(hashtag) > 140:
        return False
    return hashtag
