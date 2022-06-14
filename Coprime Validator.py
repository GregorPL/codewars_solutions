# https://www.codewars.com/kata/585c50e75d0930e6a7000336/train/python
def are_coprime(m, n):
    factors_m = []
    factors_n = []

    for i in range(m):
        if m % (i + 1) == 0:
            factors_m.append(i + 1)
    
    for i in range(n):
        if n % (i + 1) == 0:
            factors_n.append(i + 1)

    result = set(factors_m).intersection(factors_n)

    return not(max(result) > 1) 

print(are_coprime(20, 27))


