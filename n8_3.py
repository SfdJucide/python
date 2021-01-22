class ListErr(Exception):
	def __init__(self, txt):
		self.txt = txt


def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def appendarr():
	while True:
		num = input("Введите элемент >> ")
		if num == 'stop':
			break
		elif is_digit(num):
			nums.append(float(num))
		else:
			raise ListErr("Введено не число!!!")

try:
	nums = []
	appendarr()	
except ListErr as l:
	print(l)
finally:
	print(nums)