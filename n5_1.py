with open("test1.txt", "w", encoding="utf-8") as fl:
	while True:
		text = input("Введите текст в файл >> ")
		if text == "":
			break
		else:
			fl.write(text + "\n")
