from sys import argv
from itertools import count

try:
	script, start, stop = argv

	for num in count(int(start)):
		if num > int(stop):
			break
		else:
			print(num, end = " ")
except ValueError:
	print("Необходимо ввести старт и стоп (целочисленные границы)")