my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
newlist = [el for el in my_list if el != my_list[0] if my_list[my_list.index(el) - 1] < el]
print(newlist)