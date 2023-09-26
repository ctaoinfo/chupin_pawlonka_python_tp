class CurrencyConverter:
	def __init__(self, currency):
		self.currency = currency
		pass

	@property
	def currency(self):
		return self.currency

	@currency.setter
	def currency(self):
		self.currency = [
			{"name": "Euro", "value": 1}, 
			{"name": "Dollar Americain", "value": 1.0571}, 
			{"name": "Livre Sterling", "value": 0.8697},
			{"name": "Yen", "value": 157.5774},
			{"name": "Franc Suisse", "value": 0.9680},
			{"name": "Rouble Russe", "value": 102.1197},
			{"name": "Dirham Marocain", "value": 10.8502},
			{"name": "Dong Vietnamien", "value": 25 777.6167}]
		pass


	## calcul de notre valeur
	def convert_currency(self, value):
