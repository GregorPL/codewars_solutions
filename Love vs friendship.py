import string

def words_to_marks(s):
    letters = { v: k for k, v in enumerate(string.ascii_lowercase, 1) }
    
    return sum(letters[l] for l in s)

print(words_to_marks('love'))