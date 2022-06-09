def century(year):
    if year % 100 == 0:
        return int(year/100)
    else:
        return int((year/100)+1)


''' 
    best solution:
    
    def century(year):
        return (year+99)//100

'''
print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))
