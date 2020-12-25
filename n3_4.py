def pow_func(a, b, result):
	for i in range(b):
		result *= a
		
	return 1 / result


x = float(input("Введите положительное число x >> "))
y = int(input("Введите отрицательное число y >> "))

if x > 0 and y < 0:
	print(f"{x} в степени {y} = ", pow_func(x, abs(y), 1))
else:
	print("Введенны неверные данные!")
