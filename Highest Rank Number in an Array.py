def highest_rank(arr):
    count = [{"value": x, "count_num": arr.count(x)} for x in set(arr)]
    return max([i for i in count if i['count_num'] == (max(count, key=lambda x: x['count_num'])['count_num'])], key=lambda x: x['value'])['value']


arr1 = [12, 10, 8, 12, 7, 6, 4, 10, 12]  # highest rank 12
arr2 = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]  # highest rank 12
arr3 = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  # highest rank 3

print(highest_rank(arr1))
print(highest_rank(arr2))
print(highest_rank(arr3))