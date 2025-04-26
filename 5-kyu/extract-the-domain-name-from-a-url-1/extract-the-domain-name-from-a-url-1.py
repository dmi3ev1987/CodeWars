def domain_name(url):
    split_pattern = '://'
    url = split_by_pattern(url, split_pattern)
    split_pattern = 'www.'
    url = split_by_pattern(url, split_pattern)
    return url.split('.')[0]
​
​
def split_by_pattern(url, split_pattern):
    if split_pattern in url:
        url = url.split(split_pattern)[1]
    return url
​