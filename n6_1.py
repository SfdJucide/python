from time import sleep as sl


class TrafficLight:

	def __init__(self, color):
		self.__color = color



	def running(self):
		while True:
			__color = "red"
			print(__color)
			sl(7)
			__color = "yellow"
			print(__color)
			sl(2)
			__color = "green"
			print(__color)
			sl(7)
			__color = "yellow"
			print(__color)
			sl(2)


light = TrafficLight("red")
light.running()