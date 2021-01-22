class ComplexNumber:
	def __init__(self, re, im):
		self.re = re
		self.im = im

	def __str__(self):
		return f"{self.re} + {self.im}j"

	def __add__(self, other):
		return ComplexNumber(self.re + other.re, self.im + other.im)

	def __mul__(self, other):
		return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)


n1 = ComplexNumber(3, 7)
n2 = ComplexNumber(5, 0)
print("Сумма: ", n1 + n2)
print("Произведение: ", n1 * n2)