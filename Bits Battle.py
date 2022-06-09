def bits_battle(numbers):
    odds_num = [bin(i) for i in numbers if i % 2 != 0]
    even_num = [bin(i) for i in numbers if i % 2 == 0]

    odds_result = even_result = 0

    for n in odds_num:
        odds_result += len([i for i in n[2:] if i == "1"])

    for n in even_num:
        even_result += len([i for i in n[2:] if i == "0"])

    if odds_result > even_result:
        return "odds win"
    elif odds_result == even_result:
        return "tie"
    else:
        return "evens win"


print(bits_battle([5, 3, 14]))
print(bits_battle([3, 8, 22, 15, 78]))
print(bits_battle([]))
