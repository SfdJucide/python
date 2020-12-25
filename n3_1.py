
def division(a, b):
	try:
		a / b
	except ZeroDivisionError:
		return "На ноль делить нельзя!"

	return a / b

try:
	x1 = float(input("Введите делимое >> "))
	x2 = float(input("Введите делитель >> "))
	print(division(x1, x2))
except ValueError:
	print("Можно вводить только цифры!")
