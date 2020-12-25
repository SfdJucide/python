def my_func(a, b, c):
	m1 = max(a, b)
	if m1 == a:
		m2 = max(b, c)
	else:
		m2 = max(a, c)
	return m1 + m2


print("Введите поочередно 3 числа")
n1 = float(input(">> "))
n2 = float(input(">> "))
n3 = float(input(">> "))
print(my_func(n1, n2, n3))
