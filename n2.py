sec = int(input("Введите время в секундах: "))

if sec < 0:
	print("Неверные данные")
else:
	hours = sec // 3600
	minutes = (sec % 3600) // 60
	sec %= 60
	print(f"{hours:02}:{minutes:02}:{sec:02}")
