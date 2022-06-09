def get_real_floor(n):
    return n - 2 if (n >= 13) else n - 1 if (n > 0) else n


print(get_real_floor(1))
print(get_real_floor(0))
print(get_real_floor(5))
print(get_real_floor(15))
print(get_real_floor(-3))