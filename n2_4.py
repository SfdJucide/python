sentence = input("Введите строку из нескольких слов\n")
words = sentence.split()

for i in range(len(words)):
	print(f"{i + 1}) {(words[i])[0:10]}")