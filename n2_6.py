n = int(input("Введите кол-во товаров >> "))
goods = []
names = []
costs = []
counts = []
units = []

for i in range(n):

	name = input("Введите название товара >> ")
	cost = input("Введите цену товара >> ")
	count = input("Введите кол-во товара >> ")
	unit = input("Введите единицу измерения товара >> ")
	new_dict = {"название": name, "цена": cost, "количество": count, "eдиница изм.": unit}
	goods.append((i + 1, new_dict)) 
	print("-" * 30)

print(goods)

for i in range(n):

	names.append(goods[i][1].get("название"))
	costs.append(goods[i][1].get("цена"))
	counts.append(goods[i][1].get("количество"))
	units.append(goods[i][1].get("eдиница изм."))

total = {"название": names, "цена": costs, "количество": counts, "eдиница изм.": units}
print(total.items())