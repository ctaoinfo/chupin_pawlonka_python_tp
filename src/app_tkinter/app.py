from tkinter import * 
import tkinter as tk
from modules.chupin_pawlonka_TP1_B2.tp1_1_calculate import *

class Menu(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.showMenu()

	def calculateFrame(self):
		self.entry = tk.Entry(self.Frame1, width=40)
		self.entry.pack(pady=20)
		self.label = tk.Label(self.Frame1, text="")
		self.label.pack(padx=30, pady=20)
		
		self.buttonAdd = tk.Button(self.Frame2, bg="grey", text="+", command=self.choiceTp)
		self.buttonSub = tk.Button(self.Frame2, bg="grey", text="-", command=self.choiceTp)
		self.buttonDiv = tk.Button(self.Frame2, bg="grey", text="/", command=self.choiceTp)
		self.buttonMul = tk.Button(self.Frame2, bg="grey", text="x", command=self.choiceTp)
		self.buttonAdd.pack()
		self.buttonSub.pack()
		self.buttonDiv.pack()
		self.buttonMul.pack()

	def sumFactorialFrame(self):
		pass

	def conjugaitionFrame(self):
		pass

	def currencyConverterFrame(self):
		pass

	def choiceTp1(self):
		var = self.value.get()
		self.Frame1.pack_forget()
		self.Frame2.pack_forget()
		if var == "":
			pass
		elif var == "1":
			self.calculateFrame()
		elif var == "2":
			pass
		elif var == "3":
			pass
		elif var == "4":
			pass

	def choiceTp2(self):
		var = self.value.get()
		self.Frame1.pack_forget()
		self.Frame2.pack_forget()
		if var == "":
			pass
		elif var == "1":
			pass
		elif var == "2":
			pass
		elif var == "3":
			pass
		elif var == "4":
			pass

	def choiceTp3(self):
		var = self.value.get()
		self.Frame1.pack_forget()
		self.Frame2.pack_forget()
		if var == "":
			pass
		elif var == "1":
			pass
		elif var == "2":
			pass
		elif var == "3":
			pass
		elif var == "4":
			pass
	
	def choiceTp4(self):
		var = self.value.get()
		self.Frame1.pack_forget()
		self.Frame2.pack_forget()
		if var == "":
			pass
		elif var == "1":
			pass
		elif var == "2":
			pass
		elif var == "3":
			pass
		elif var == "4":
			pass

	def choiceTp(self):
		print(self.value.get())
		var = self.value.get()
		if var == "":
			pass
		elif var == "1":
			self.button1.config(text="TP 1.1 - Calculatrice")
			self.button2.config(text="TP 1.2 - Somme & Factoriel")
			self.button3.config(text="TP 1.3 - Conjugaison")
			self.button4.config(text="TP 1.4 - Convertisseur de devise")
			self.button.config(command=self.choiceTp1)
		elif var == "2":
			self.button1.config(text="TP 2.1 - ")
			self.button2.config(text="TP 2.2 - ")
			self.button3.config(text="TP 2.3 - ")
			self.button4.config(text="TP 2.4 - ")
			self.button.config(command=self.choiceTp2)
		elif var == "3":
			self.button1.config(text="TP 3.1 - ")
			self.button2.config(text="TP 3.2 - ")
			self.button3.config(text="TP 3.3 - ")
			self.button4.config(text="TP 3.4 - ")
			self.button.config(command=self.choiceTp3)
		elif var == "4":
			self.button1.config(text="TP 4.1 - ")
			self.button2.config(text="TP 4.2 - ")
			self.button3.config(text="TP 4.3 - ")
			self.button4.config(text="TP 4.4 - ")
			self.button.config(command=self.choiceTp4)		

	def showMenu(self):
		self.value = StringVar()
		self.value.set("")
		# frame 1
		self.Frame1 = tk.Frame(self, borderwidth=2, relief=GROOVE)
		self.Frame1.pack(side=LEFT, padx=30, pady=30)

		# frame 2
		self.Frame2 = tk.Frame(self, borderwidth=2, relief=GROOVE)
		self.Frame2.pack(side=LEFT, padx=10, pady=10)
			
		# Ajout de labels
		tk.Label(self.Frame1, text="Quels TP choisir").pack(padx=10, pady=10)

		# radiobutton
		value = StringVar() 
		self.button1 = tk.Radiobutton(self.Frame1, text="TP 1", variable=self.value, value="1")
		self.button2 = tk.Radiobutton(self.Frame1, text="TP 2", variable=self.value, value="2")
		self.button3 = tk.Radiobutton(self.Frame1, text="TP 3", variable=self.value, value="3")
		self.button4 = tk.Radiobutton(self.Frame1, text="TP 4", variable=self.value, value="4")
		self.button1.pack()
		self.button2.pack()
		self.button3.pack()
		self.button4.pack()
		
		# bouton de sortie
		self.button = tk.Button(self.Frame2, bg="grey", text="Séléctionner", command=self.choiceTp)
		self.button.pack()

		self.exitButton = tk.Button(self.Frame2, bg="grey", text="Quitter", command=self.destroy)
		self.exitButton.pack()