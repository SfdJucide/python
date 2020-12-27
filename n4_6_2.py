from sys import argv
from itertools import cycle

try:
	script, s1, s2, s3, s4, s5, stop = argv

	arr = [s1, s2, s3, s4, s5]
	i = 0
	for el in cycle(arr):
		if i == int(stop):
			break
		else:
			print(el)
		i += 1
except ValueError:
	print("Необходимо ввести 5 любых элементов списка и целочисленную стоп - границу!")