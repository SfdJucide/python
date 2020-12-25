def info(v2, v3, v5, v1, v6, v4):
	print(f"{v1} {v2} {v3} г. место жительства - {v4}, контакты: {v5} {v6}")


name = input("Введите ваше имя >> ")
surname = input("Введите фамицию >> ")
year = int(input("Введите год вашего рождения >> "))
hometown = input("Введите ваш город проживания >> ")
email = input("Введите ваш email >> ")
phone_number = input("Введите ваш телефонный номер >> ")

info(v1 = name, v2 = surname, v3 = year, v4 = hometown, v5 = email, v6 = phone_number)