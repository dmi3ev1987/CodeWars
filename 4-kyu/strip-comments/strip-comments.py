def strip_comments(input_string, markers_list):
    string_lines = input_string.split('\n')
    for marker in markers_list:
        string_lines = [
            line.split(marker)[0].rstrip() for line in string_lines
        ]
    return '\n'.join(string_lines)
