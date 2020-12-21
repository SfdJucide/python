mass = []
print("Ввод элементов списка, для окончания ввода нажмите Enter")
while True:
	element = input(">>")
	if element:
		mass.append(element)
	else:
		break
print(mass)
for i in range (0, len(mass) - 1, 2):
	t = mass[i]
	mass[i] = mass[i+1]
	mass[i+1] = t
print(mass)
