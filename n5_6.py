new_dict = {}

with open("desktop\\test6.txt", "r", encoding="utf-8") as fl:
	for i in fl:
		i = i.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace(':', '').replace('—', '0').replace('.', '')
		subject = i.split()
		new_dict[subject[0]] = sum(map(int, subject[1:]))
	print(new_dict)

