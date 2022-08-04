def make_chocolates(s, b, g):
    for i in range(b, -1, -1):
        for y in range(s + 1):
            if (b * 5 + y * 2) == g: return y
        
        else:
            return -1

print(make_chocolates(8, 15, 3))

