from sys import argv

try:
	name, hours, sph, premium = argv
	print(f"Зарплата сотрудника будет составлять: {int(hours) * int(sph) + int(premium)}")
except ValueError:
	print("Ожидается ввод 4 целочисленных аргументов!")
