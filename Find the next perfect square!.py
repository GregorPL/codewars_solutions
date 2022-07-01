# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

def find_next_square(sq):
    return int(((sq ** (1/2))+ 1) ** 2) if (sq ** (1/2)).is_integer()  else -1

print(find_next_square(114))
 