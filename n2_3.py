seasons = {1: "Зима", 2: "Весна",
			3: "Лето", 4: "Осень"}
months = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10 , 11]]
month = int(input("Введите месяц в виде числа от 1 до 12\n"))
if  1 <= month <= 12:
	for i in range(4):
		for j in range(3):
			if month == months[i][j]:
				print("Ваш месяц относится к времени года:", seasons.get(i + 1))
else:
	print("Введены неверные данные")