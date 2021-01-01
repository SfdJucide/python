try:
	with open("test3.txt", "r", encoding="utf-8") as fl:
		data = fl.readlines()
		print("Сотрудники с окладом менее 20000:")
		summ = 0
		for i in data:
			info = i.split()
			if int(info[1]) < 20000:
				print(info[0])
			summ += int(info[1])

		print(f"Средняя величина дохода сотрудников: {summ / len(data):.2f}")

except FileNotFoundError as f:
	print(f)
except ValueError as err:
	print(err)