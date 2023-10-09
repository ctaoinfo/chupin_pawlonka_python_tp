from tkinter import * 
import tkinter as tk
from tkinter import messagebox
from modules.chupin_pawlonka_TP1_B2.tp1_1_calculate import *

class Menu(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.geometry('300x200') 
		self.showMenu()

	def calculateFrame(self):

		self.geometry('600x600')

		# frame 1
		self.Frame1 = tk.Frame(self, borderwidth=2, relief=GROOVE)
		self.Frame1.pack(side=LEFT, padx=30, pady=30)

		# frame 2
		self.Frame2 = tk.Frame(self, borderwidth=2, relief=GROOVE)
		self.Frame2.pack(side=LEFT, padx=10, pady=10)
			
		calc = Calculate
		calc.result = 0
		self.entry = tk.Entry(self.Frame1, width=40)
		self.entry.pack(pady=20)
		self.label = tk.Label(self.Frame1, text=calc.result)
		self.label.pack(padx=30, pady=20)
		calc.result = self.entry.get()
		self.buttonAdd = tk.Button(self.Frame2, bg="grey", text="+", command=calc.addition)
		self.buttonSub = tk.Button(self.Frame2, bg="grey", text="-", command=calc.substraction)
		self.buttonDiv = tk.Button(self.Frame2, bg="grey", text="/", command=calc.division)
		self.buttonMul = tk.Button(self.Frame2, bg="grey", text="x", command=calc.multiplication)
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
		self.Frame1.destroy()
		self.Frame2.destroy()
		if var == "":
			pass
		elif var == "1":
			self.calculateFrame()
		elif var == "2":
			self.error()
		elif var == "3":
			self.error()
		elif var == "4":
			self.error()

	def choiceTp2(self):
		var = self.value.get()
		self.Frame1.destroy()
		self.Frame2.destroy()
		if var == "":
			self.error()
		elif var == "1":
			self.error()
		elif var == "2":
			self.error()
		elif var == "3":
			self.error()
		elif var == "4":
			self.error()

	def choiceTp3(self):
		var = self.value.get()
		self.Frame1.destroy()
		self.Frame2.destroy()
		if var == "":
			self.error()
		elif var == "1":
			self.error()
		elif var == "2":
			self.error()
		elif var == "3":
			self.error()
		elif var == "4":
			self.error()
	
	def choiceTp4(self):
		var = self.value.get()
		self.Frame1.destroy()
		self.Frame2.destroy()
		if var == "":
			self.error()
		elif var == "1":
			self.error()
		elif var == "2":
			self.error()
		elif var == "3":
			self.error()
		elif var == "4":
			self.error()

	def choiceTp(self):
		print(self.value.get())
		var = self.value.get()

		if var == "":
			return
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
			self.button.config(command=self.error)
		elif var == "3":
			self.button1.config(text="TP 3.1 - ")
			self.button2.config(text="TP 3.2 - ")
			self.button3.config(text="TP 3.3 - ")
			self.button4.config(text="TP 3.4 - ")
			self.button.config(command=self.error)
		elif var == "4":
			self.button1.config(text="TP 4.1 - ")
			self.button2.config(text="TP 4.2 - ")
			self.button3.config(text="TP 4.3 - ")
			self.button4.config(text="TP 4.4 - ")
			self.button.config(command=self.error)

		self.geometry('400x200')
		self.Returnbutton = tk.Button(self.Frame2, bg="grey", text="Retour", command=self.showMenu)
		self.Returnbutton.pack()	

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
		tk.Label(self.Frame1, text="Quel TP choisir").pack(padx=10, pady=10)

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

		self.exitButton = tk.Button(self.Frame2, bg="grey", text="Quitter", command=self.ExitApp)
		self.exitButton.pack()

	def error(self):
		tk.messagebox.showinfo(title='Error', message='TP indisponible')

	def ExitApp(self):
		MsgBox = tk.messagebox.askquestion('Quitter','Voulez-vous vraiment quitter ?',icon = 'error')
		if MsgBox == 'yes':
			self.destroy()
		else:
			tk.messagebox.showinfo('De retour ?','Finalement le canard était bon ?')