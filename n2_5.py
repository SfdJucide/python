raiting = [7, 5, 3, 3, 2]
newNum = "1"

while True:
	newNum = int(input("Введите новый элемент рейтинга >> "))
	if raiting[0] < newNum:
		raiting.insert(0, newNum)
	elif raiting[len(raiting) - 1] >= newNum:
		raiting.insert(len(raiting), newNum)
	else:
		for i in range(len(raiting) - 1):
			if raiting[i] >= newNum > raiting[i + 1]:
				raiting.insert(i + 1, newNum)
				break

	print(raiting)