def int_func(text):
	for i in range(len(text)):
		latin = 0
		word = list(text[i])
		for j in range(len(word)):
			if 96 < ord(word[j]) < 123:
				latin += 1

			if latin == len(word):
				word[0] = chr(ord(word[0]) - 32)
				for g in range(len(word)):
					print(word[g], end = "")

				print(" ", end = "")


sentence = input("Введите предложение\n").split()
int_func(sentence)
