class Worker:

	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

	def get_full_name(self):
		print(f"Full name: {self.name} {self.surname}")


	def get_total_income(self):
		print(f"Position: {self.position}")
		print(f"Income: {sum(self._income.values())}")


try:
	n = input("Введите имя сотрудника >> ")
	s = input("Введите фамилию сотрудника >> ")
	p = input("Введите должность сотрудника >> ")
	w = int(input("Введите оклад сотрудника >> "))
	b = int(input("Введите премию сотрудника >> "))

	info = Position(n, s, p, w, b)
	info.get_full_name()
	info.get_total_income()
except ValueError:
	print("ValueError!")
