class Date:
	def __init__(self, day, month, year):
		self.year = year
		self.month = month
		self.day = day

	@classmethod
	def to_int(cls, date):
		a, b, c = date.split('-')
		return cls(int(a), int(b), int(c))

	@staticmethod
	def create_date(obj):
		if obj.year <= 0 or obj.year > 2021:
			return "Uncorrect year"
		elif obj.month > 12 or obj.month <= 0:
			return "Uncorrect month"
		elif obj.day > 31 or obj.day <= 0:
			return "Uncorrect day"
		else:
			return f"{obj.day}-{obj.month}-{obj.year} is correct date!"


date = input("Введите дату в формате «день-месяц-год»\n")
d = Date.to_int(date)
print(Date.create_date(d))