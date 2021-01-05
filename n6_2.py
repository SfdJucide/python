class Road:

	def __init__(self, length, width):
		self._length = length
		self._width = width
		self.depth = 5
		self.mass = 25


	def total_mass(self):
		return self._length * self._width * self.depth * self.mass / 1000


try:
	a = int(input("Введите длинну покрытия >> "))
	b = int(input("Введите ширину покрытия >> "))
	result = Road(a, b)
	print(f"{result.total_mass():.0f} т")
except ValueError as e:
	print("Только числа!")
