from random import randint

with open("test5.txt", "w", encoding="utf-8") as fl:
	nums = [randint(1, 500) for i in range(500)]
	fl.write(" ".join(map(str, nums)))
	summ = sum(nums)

print(f"Сумма чисел в файле равна: {summ}")
