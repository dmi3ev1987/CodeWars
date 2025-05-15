def get_middle(string):
    lenght = len(string)
    if lenght % 2:
        return string[lenght//2:(lenght//2)+1]
    return string[(lenght//2)-1:(lenght//2)+1]