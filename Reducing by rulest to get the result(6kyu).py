from itertools import cycle

def reduce_by_rules(lst, rules):
    
    i = 0
    
    while len(lst) > 1:
        
        lst = [rules[i](lst[0], lst[1])] + lst[2:]
        
        if i + 1 == len(rules):
            i = 0
        else:
            i += 1
        
    return lst[0]

print(reduce_by_rules([2.0, 2.0, 3.0, 4.0], [lambda a, b: a + b, lambda a, b: a - b]))