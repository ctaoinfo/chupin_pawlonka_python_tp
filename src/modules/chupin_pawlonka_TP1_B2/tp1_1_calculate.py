class Calculate:
	def __init__(self, number, result):
		self.number = number
		self.result = result

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

	def addition(self):
		self.result += self.number

	def substraction(self):
		self.result -= self.number

	def multiplication(self):
		self.result *= self.number

	def division(self):
		self.result /= self.number