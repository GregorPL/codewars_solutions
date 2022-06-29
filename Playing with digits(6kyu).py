#https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dif_pow(n, p):
    result = 0

    for i in list(str(n)):
        result += pow(int(i), p)
        p += 1
    
    rest = result % n

    if rest == 0:
        return result // n
    else:
        return -1