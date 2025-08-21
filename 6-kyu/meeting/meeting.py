def meeting(input_string):
    return ''.join(
        f'({name[0]}, {name[1]})'
        for name in sorted(
            friend.split(':')[::-1]
            for friend in input_string.upper().split(';')
        )
    )