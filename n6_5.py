class Stationery:

	def __init__(self, title):
		self.title = title

	def draw(self):
		print("Запуск отрисовки")


class Pen(Stationery):

	def draw(self):
		print(f"Инструмент: {self.title}")
		print("Чертим аккуратную тонкую линиию")


class Pencil(Stationery):

	def draw(self):
		print(f"Инструмент: {self.title}")
		print("Чертим среднюю серую линиию")


class Handle(Stationery):

	def draw(self):
		print(f"Инструмент: {self.title}")
		print("Чертим жирную яркую линиию")



tool = int(input("Чем вы хотите рисовать?\n1.Ручка\n2.Карандаш\n3.Маркер\n"))
if tool == 1:
	tool = Pen("Ручка")
	tool.draw()
elif tool == 2:
	tool = Pencil("Карандаш")
	tool.draw()
elif tool == 3:
	tool = Handle("Маркер")
	tool.draw()
else:
	print("Введенны неверные данные!")