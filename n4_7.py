from sys import argv

try:
	script, n = argv

	def factorial(n):
		new_gen = (el for el in range(n + 1))
		for fact in new_gen:
			yield fact
		

	for num in factorial(int(n)):
		fact = 1
		for j in range(1, num + 1):
			fact *= j
		print(f"{num}! = {fact}")

except ValueError:
	print("Введите целое число для нахождения факториала")
