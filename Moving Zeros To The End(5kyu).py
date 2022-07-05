# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):

    for i in range(lst.count(0)):
        lst.remove(0)
        lst.append(0)