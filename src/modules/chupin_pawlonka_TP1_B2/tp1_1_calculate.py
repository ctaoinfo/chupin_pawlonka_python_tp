class Calculate:
	def __init__(self, number, result):
		self.number = number
		self.result = result

	@property
	def number(self):
		return self.number

	@number.setter
	def number(self, values):
		self.number = values
		pass

	@property
	def result(self):
		return self.result

	@result.setter
	def result(self, value):
		self.result = value
		pass

	def addition(self):
		self.result += self.number
		pass

	def substraction(self):
		self.result -= self.number
		pass

	def multiplication(self):
		self.result *= self.number
		pass

	def division(self):
		self.result /= self.number
		pass