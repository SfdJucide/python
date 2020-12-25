def sum():
	s = 0
	while True:
		nums = input("Введите числа через пробел, для выхода нажмите \"!\"\n").split()
		for i in nums:
			if i == "!":
				return s
			else:
				try:
					s += float(i)
				except ValueError:
					pass

		print(s)


print(sum())