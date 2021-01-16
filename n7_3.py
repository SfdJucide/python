class Cell:
	def __init__(self, n):
		self.n = n

	def __add__(self, other):
		return self.n + other.n


	def __sub__(self, other):
		if self.n >= other.n:
			return self.n - other.n
		else:
			return other.n - self.n


	def __mul__(self, other):
		return self.n * other.n


	def __floordiv__(self, other):
		return self.n // other.n


	def make_order(self, row):
		count = self.n // row
		for i in range(count):
			print("*" * row)
		print("*" * (self.n % row))


cell_1 = Cell(13)
cell_2 = Cell(9)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
cell_1.make_order(3)
print()
cell_2.make_order(4)

