class ZeroDivisionErr(Exception):
	def __init__(self, txt):
		self.txt = txt

try:
	a = int(input("Введите делимое >> "))
	b = int(input("Введите делитель >> "))
	if b == 0 and a != 0:
		print("Меняем местами члены из-за возможной ошибки!")
		a, b = b, a
	elif a == 0 and b == 0:
		raise ZeroDivisionErr("Невозможно деление на ноль!")
except ValueError:
	print("Введено не число!")
except ZeroDivisionErr as z:
	print(z)
else:
	print(a / b)