#https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
    res = []

    for ch in list(iterable):
        if len(res) > 0:
            if res[-1] != ch:
                res.append(ch)
        else:
            res.append(ch)

    return res