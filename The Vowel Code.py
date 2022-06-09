vowels_to_num = {
    "a": "1",
    "e": "2",
    "i": "3",
    "o": "4",
    "u": "5"
}


def encode(st):
    for old, new in vowels_to_num.items():
        st = st.replace(old, new)
    return st


def decode(st):
    for old, new in vowels_to_num.items():
        st = st.replace(new, old)
    return st


print(encode('hello'))