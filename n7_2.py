from abc import ABC, abstractmethod
from random import randint as rand

class Clothes(ABC):

	@abstractmethod
	def consump(self):
		pass


class Coat(Clothes):
	def __init__(self, v):
		self.v = v

	@property
	def consump(self):
		return self.v / 6.5 + 0.5


class Costume(Clothes):
	def __init__(self, h):
		self.h = h

	@property
	def consump(self):
		return 2 * self.h + 0.3


a = Coat(56)
print(f"Расход ткани на 1 пальто: {a.consump:.2f}")
b = Costume(181)
print(f"Расход ткани на 1 костюм: {b.consump:.2f}")

#для случайого кол-ва пальто\костюмов
print(f"Общий расход ткани: {(a.consump * rand(1, 101) + b.consump * rand(1, 101)):.2f}")
