class Matrix:
	def __init__(self, matrix, n):
		self.matrix = matrix
		self.n = n

	def __str__(self):
		print(f"Матрица: {self.n}")
		return '\n'.join('\t'.join(map(str, line)) for line in self.matrix)

	def __add__(self, other):
		print("Сумма матриц:")
		res = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
		return res

arr = [[3, 4], [56, 7], [-3, 78]]
arr2 = [[10, 9], [8, 15], [0, 98]]
mc = Matrix(arr, 1)
print(mc)
mc2 = Matrix(arr2, 2)
print(mc2)

if len(arr) == len(arr2):
	m = 0
	for i in range(len(arr)):
		if len(arr[i]) == len(arr2[i]):
			m += 1

	if m == len(arr):
		summ = Matrix(mc + mc2, 3)
		print(summ)
