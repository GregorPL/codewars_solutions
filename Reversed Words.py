def reverse_words(s):
    s = s.split(" ")
    s.reverse()
    return " ".join(s)


print(reverse_words("The greatest victory is that which requires no battle"))

str = "The greatest victory is that which requires no battle"

str = str.split(" ")
print(str[::-1])