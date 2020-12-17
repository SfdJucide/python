proceeds = int(input("Введите значение выручки фирмы: "))
cost = int(input("Введите значение издержек фирмы: "))

if proceeds >= 0 and cost >= 0:
	if proceeds > cost:
		print("Фирма работает в прибыль")
		print(f"Прибыль равна {proceeds - cost}")
		rent = (proceeds - cost) / proceeds * 100
		print(f"Рентабельность выручки равна {rent:.2f}%")
		count = int(input("Введите кол-во сотрудников фирмы: "))
		profit = (proceeds - cost) / count 
		print(f"Прибыль фирмы в расчете на одного сотрудника равна {profit:.1f}")

	elif proceeds < cost:
		print("Фирма работает в убыток")
		print(f"Убыток равнен {cost - proceeds}")
	else:
		print("Фирма работает в ноль")
else:
	print("Введены неверные данные")