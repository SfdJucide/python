num = int(input("Введите целое положительное число: "))
maxNum = 0;

while num:
	if (num % 10) > maxNum:
		maxNum = num % 10
	num //= 10

print(f"Наибольшая цифра числа = {maxNum}")
