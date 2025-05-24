def strip_comments(input_string, markers_list):
    string_lines = input_string.split('\n')
    for index in range(len(string_lines)):
        for marker in markers_list:
            string_lines[index] = str(string_lines[index]).split(marker)[0].rstrip()
    return '\n'.join(string_lines)