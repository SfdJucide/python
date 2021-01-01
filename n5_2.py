try:
	with open("test2.txt", "r", encoding="utf-8") as fl:
		strings = fl.readlines()
		c = 0
		for i in strings:
			c += 1
			words = (i.split())
			print(f"Строка №{c}: кол-во слов({len(words)}), кол-во символов({len(i)})")

except FileNotFoundError as f:
	print(f)
