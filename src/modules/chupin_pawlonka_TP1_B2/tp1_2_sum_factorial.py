class SumAndFactorial:
	def __init__(self, number, result, list_numbers):
		self.number = number
		self.result = result
		self.list_numbers = list_numbers

	@property
	def number(self):
		return self.number

	@number.setter
	def number(self, value):
		self.number = value

	@property
	def result(self):
		return self.result

	@result.setter
	def result(self, value):
		self.result = value
		pass

	@property
	def list_numbers(self):
		return self.list_numbers

	@list_numbers.setter
	def list_numbers(self, values):
		self.list_numbers = values

	def sum(self, self.number, self.result):
		for x in range(self.number):
			self.result += x

	def factorial(self, self.number, self.result):
		for x in range(self.number):
			self.result *= x