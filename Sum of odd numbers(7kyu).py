# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
def row_sum_odd_numbers(n):
    s = n * n - (n - 1)
    return sum(s + (x + x) for x in range(n))

print(row_sum_odd_numbers(2))

 
