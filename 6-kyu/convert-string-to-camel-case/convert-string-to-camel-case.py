import re
​
​
def to_camel_case(text):
    text_list = re.split(r'[_\-]', text)
    result_text = ""
    for index in range(len(text_list)):
        if index == 0:
            result_text += text_list[index]
        else:
            result_text += text_list[index].capitalize()
    return result_text
​