from string import ascii_lowercase


def is_pangram(st):
    letters_present = dict.fromkeys(ascii_lowercase, 0)
    for letter in st.lower():
        if letter in letters_present:
            letters_present[letter] += 1
    return all(letters_present.values())
