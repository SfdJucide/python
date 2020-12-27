arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_arr = [i for i in arr if arr.count(i) == 1]
print(new_arr)