class Warehouse:
	store = {'printer': [], 'scanner': [], 'xerox': []}
	units = {'main_office': [], 'south_office': [], 'new_north_office': []}

	def add_to_store(self, eq, name, count, cost, special):
		self.store[eq].append([name, count, cost, special])
		print(self.store)
		

	def trans_to_unit(self, office, eq, name, count, cost, special):
		self.units[office].append({eq: [name, count, cost, special]})
		print(self.units)


class Equipment:
	def __init__(self, name, count, cost):
		self.name = name
		self.cost = cost
		self.count = count


class Printer(Equipment):
	def __init__(self, name, count, cost, print_tech):
		super().__init__(name, count, cost)
		self.pt = print_tech


class Scanner(Equipment):
	def __init__(self, name, count, cost, dpi):
		super().__init__(name, count, cost)
		self.dpi = dpi


class Xerox(Equipment):
	def __init__(self, name, count, cost, speed):
		super().__init__(name, count, cost)
		self.speed = speed


try:
	while True:
		choice = int(input("Выберите вид оргтехники:\n1.Printer\n2.Scanner\n3.Xerox\n"))
		if choice == 1:
			model = input("Введите модель техники >> ")
			count = int(input("Введите кол-во техники >> "))
			cost = int(input("Введите цену техники >> "))
			pt = input("Введите технику печати техники >> ")
			eq = Printer(model, count, cost, pt)

			choice = int(input("Что вы хотите сделать с техникой?\n1.Поместить на склад\n2.Транспортировать\n"))
			wh = Warehouse()
			if choice == 1:
				wh.add_to_store('printer', eq.name, eq.count, eq.cost, eq.pt)
			elif choice == 2:
				choice = int(input("В какой фелиал?\n1.Главный оффис\n2.Южный оффис\n3.Новый северный оффис\n"))
				if choice == 1:
					wh.trans_to_unit('main_office', 'printer', eq.name, eq.count, eq.cost, eq.pt)
				elif choice == 2:
					wh.trans_to_unit('south_office', 'printer', eq.name, eq.count, eq.cost, eq.pt)
				elif choice == 3:
					wh.trans_to_unit('new_north_office', 'printer', eq.name, eq.count, eq.cost, eq.pt)
				else:
					raise ValueError
			else:
				raise ValueError
		elif choice == 2:
			model = input("Введите модель техники >> ")
			count = int(input("Введите кол-во техники >> "))
			cost = int(input("Введите цену техники >> "))
			dpi = input("Введите глубину печати техники >> ")
			eq = Scanner(model, count, cost, dpi)

			choice = int(input("Что вы хотите сделать с техникой?\n1.Поместить на склад\n2.Транспортировать\n"))
			wh = Warehouse()
			if choice == 1:
				wh.add_to_store('scanner', eq.name, eq.count, eq.cost, eq.dpi)
			elif choice == 2:
				choice = int(input("В какой фелиал?\n1.Главный оффис\n2.Южный оффис\n3.Новый северный оффис\n"))
				if choice == 1:
					wh.trans_to_unit('main_office', 'scanner', eq.name, eq.count, eq.cost, eq.dpi)
				elif choice == 2:
					wh.trans_to_unit('south_office', 'scanner', eq.name, eq.count, eq.cost, eq.dpi)
				elif choice == 3:
					wh.trans_to_unit('new_north_office', 'scanner', eq.name, eq.count, eq.cost, eq.dpi)
				else:
					raise ValueError
			else:
				raise ValueError
		elif choice == 3:
			model = input("Введите модель техники >> ")
			count = int(input("Введите кол-во техники >> "))
			cost = int(input("Введите цену техники >> "))
			speed = input("Введите скорость печати техники >> ")
			eq = Xerox(model, count, cost, speed)

			choice = int(input("Что вы хотите сделать с техникой?\n1.Поместить на склад\n2.Транспортировать\n"))
			wh = Warehouse()
			if choice == 1:
				wh.add_to_store('xerox', eq.name, eq.count, eq.cost, eq.speed)
			elif choice == 2:
				choice = int(input("В какой фелиал?\n1.Главный оффис\n2.Южный оффис\n3.Новый северный оффис\n"))
				if choice == 1:
					wh.trans_to_unit('main_office', 'xerox', eq.name, eq.count, eq.cost, eq.speed)
				elif choice == 2:
					wh.trans_to_unit('south_office', 'xerox', eq.name, eq.count, eq.cost, eq.speed)
				elif choice == 3:
					wh.trans_to_unit('new_north_office', 'xerox', eq.name, eq.count, eq.cost, eq.speed)
				else:
					raise ValueError
			else:
				raise ValueError
		else:
			break
except ValueError:
	print("Введенны недопустимые значения!")
