from random import choice
from time import sleep

class Car:

	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police


	def go(self):
		print(f"Машина {self.name} поехала!")
		Car(self.speed, self.color, self.name, self.is_police).turn("прямо")


	def stop(self):
		print(f"Машина {self.name} остановилась!")


	def turn(self, direction):
		for i in range(5):
			print(f"Машина едет {direction}")
			move = ["влево", "вправо", "назад"]
			print(f"Машина повернула {choice(move)}")
			sleep(5)


	def show_speed(self):
		print(f"Машина едет со скоростью {self.speed} км/ч")


class TownCar(Car):
	
	def show_speed(self):
		if self.speed > 60:
			print("Превышение скорости!")
		else:
			super().show_speed()


class SportCar(Car):
	pass


class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40:
			print("Превышение скорости!")
		else:
			super().show_speed()


class PoliceCar(Car):
	pass


try:
	s = int(input("Введите скорость >> "))
	c = input("Введите цвет машины >> ")
	n = input("Введите название машины >> ")
	p = input("Машина полицейкая? >> ")

	if p.lower() == "да":
		cars = PoliceCar(s, c, n, True)
	elif p.lower() == "нет":
		names = [WorkCar(s, c, n, False), SportCar(s, c, n, False), TownCar(s, c, n, False)]
		cars = choice(names)

	cars.go()
	cars.show_speed()
	cars.stop()
except ValueError:
	print("ValueError")

