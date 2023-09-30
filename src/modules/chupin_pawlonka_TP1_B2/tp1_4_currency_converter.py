from currency_converter import CurrencyConverter

class CurrencyConverter:
	def __init__(self, _initCurrency, _toCurrency, _currencies):
		self._currencies = CurrencyConverter().currencies
		self._initCurrency = _initCurrency
		self._toCurrency = _toCurrency

	@property
	def initCurrency(self):
		return self._initCurrency

	@property
	def toCurrency(self):
		return self._toCurrency

	@initCurrency.setter
	def initCurrency(self, value):
		self._initCurrency = value

	@toCurrency.setter
	def toCurrency(value, value):
		self._toCurrency = value

	def converter(self, value):
		return CurrencyConverter().convert(value, self._initCurrency, self._toCurrency)

	co