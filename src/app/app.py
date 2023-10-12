import os
from modules.chupin_pawlonka_TP1_B2.tp1_1_calculate import *

class App:
	def Init(self):
		pass

	def ChangeMenu(self):
		pass
		
# 	def __init__(self):
# 		while True:
# 			os.system('clear')
# 			print('1. TP1')
# 			print('2. TP2')
# 			print('3. TP3')
# 			print('4. TP4')
# 			print('\t0. Quitter\n')
# 			choiceTP = input('Quel TP choisir: ')
# 			if choiceTP == '0':
# 				os.system('clear')
# 				print('Merci d\'être passé')
# 				exit()
# 			elif choiceTP == '1':
# 				self.tp1()
# 			elif choiceTP == '2':
# 				self.tp2()
# 			elif choiceTP == '3':
# 				pass
# 			elif choiceTP == '4':
# 				pass


# 	def tp1(self):
# 		while True:
# 			os.system('clear')
# 			print('1.1 - Calculatrice')
# 			print('1.2 - Somme & Factoriel')
# 			print('1.3 - Conjugaison')
# 			print('1.4 - Convertisseur de devise')
# 			print('\t0. Retour\n')
# 			choiceTP = input('Quel TP choisir: ')
# 			if choiceTP == '0':
# 				os.system('clear')
# 				break
# 			elif choiceTP == '1':
# 				self.tp11()
# 			elif choiceTP == '2':
# 				self.tp12()
# 			elif choiceTP == '3':
# 				self.tp13()
# 			elif choiceTP == '4':
# 				self.tp14()

# 	def tp2(self):
# 		while True:
# 			os.system('clear')
# 			print('2.1 - Test Nombre Premier')
# 			print('2.2 - Calcul Moyenne & Médiane')
# 			print('2.3 - Calcul Variance et Ecart-Type')
# 			print('2.4 - Analyse Données d\'Âge')
# 			print('2.5 - Simulation lancers de dés')
# 			print('\t0. Retour\n')
# 			choiceTP = input('Quel TP choisir: ')
# 			if choiceTP == '0':
# 				os.system('clear')
# 				break
# 			elif choiceTP == '1':
# 				pass
# 			elif choiceTP == '2':
# 				pass
# 			elif choiceTP == '3':
# 				pass
# 			elif choiceTP == '4':
# 				pass
# 			elif choiceTP == '5':
# 				pass

# 	def tp3(self):
# 		pass

# 	def tp11(self):
# 		calc = Calculate()
# 		print('\nCalculatrice\n')
# 		while True:
# 			calc.number = input('= ')
# 			calc.result = calc.number()
# 			print('\t+ - / *')
# 			nb = input(" ")
# 			if nb == '+':
# 				calc.number = input(' ')
# 				calc.addition()
# 			elif nb == '-':
# 				calc.number = input(' ')
# 				calc.substraction()
# 			elif nb == '*':
# 				calc.number = input(' ')
# 				calc.multiplication()
# 			elif nb == '/':
# 				calc.number = input(' ')
# 				calc.substraction()
# 			print(calc.result)

# 	def tp12(self):
# 		pass

# 	def tp13(self):
# 		pass

# 	def tp14(self):
# 		pass

# 	def tp21(self):
# 		pass

# 	def tp22(self):
# 		pass

# 	def tp23(self):
# 		pass

# 	def tp24(self):
# 		pass

# 	def tp25(self):
# 		pass