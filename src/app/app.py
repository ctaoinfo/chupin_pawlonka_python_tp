import os
from modules.chupin_pawlonka_TP1_B2.tp1_1_calculate import *

class App:
	def __init__(self):
		while True:
			os.system('clear')
			print('1. TP1')
			print('2. TP2')
			print('3. TP3')
			print('4. TP4')
			print('\t0. Quitter\n')
			choiceTP = input('Quel TP choisir: ')
			if choiceTP == '0':
				os.system('clear')
				print('Merci d\'être passé')
				exit()
			elif choiceTP == '1':
				self.tp1()
			elif choiceTP == '2':
				self.tp2()
			elif choiceTP == '3':
				self.tp3()


	def tp1(self):
		while True:
			os.system('clear')
			print('1.1 - Calculatrice')
			print('1.2 - Somme & Factoriel')
			print('1.3 - Conjugaison')
			print('1.4 - Convertisseur de devise')
			print('\t0. Retour\n')
			choiceTP = input('Quel TP choisir: ')
			if choiceTP == '0':
				os.system('clear')
				break
			elif choiceTP == '1':
				self.tp11()
			elif choiceTP == '2':
				pass
			elif choiceTP == '3':
				pass

	def tp2(self):
		pass

	def tp3(self):
		pass

	def tp11(self):
		calc = Calculate
		print('\nCalculatrice\n')
		while True:
			calc.number = input('= ')
			calc.result = calc.number
			print('\t\t+')
			print('\t\t-')
			print('\t\t*')
			print('\t\t/')
			nb = input(" ")
			if nb == '+':
				calc.addition()
			elif nb == '-':
				calc.substraction()
			elif nb == '*':
				calc.multiplication()
			elif nb == '/':
				calc.substraction()
			calc.number = input(' ')
			print(calc.result)

	def tp12(self):
		pass

	def tp13(self):
		pass

	def tp14(self):
		pass