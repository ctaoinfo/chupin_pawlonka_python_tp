from tkinter import *
from tkinter.messagebox import *
from .app import *

class Menu(App):
	# frame 1
	Frame1 = Frame(self, borderwidth=2, relief=GROOVE)
	Frame1.pack(side=LEFT, padx=30, pady=30)

	# frame 2
	Frame2 = Frame(self, borderwidth=2, relief=GROOVE)
	Frame2.pack(side=LEFT, padx=10, pady=10)
		
	# Ajout de labels
	Label(Frame1, text="Quels TP choisir").pack(padx=10, pady=10)

	# radiobutton
	value = StringVar() 
	button1 = Radiobutton(Frame1, text="TP 1", variable=value, value=1)
	button2 = Radiobutton(Frame1, text="TP 2", variable=value, value=2)
	button3 = Radiobutton(Frame1, text="TP 3", variable=value, value=3)
	button4 = Radiobutton(Frame1, text="TP 4", variable=value, value=4)
	button1.pack()
	button2.pack()
	button3.pack()
	button4.pack()

	def choiceTp(self):
		var = value.get()
		if var == "":
			pass
		elif var == "1":
			button1.config(text="TP 1.1 - Calculatrice")
			button2.config(text="TP 1.2 - Somme & Factoriel")
			button3.config(text="TP 1.3 - Conjugaison")
			button4.config(text="TP 1.4 - Convertisseur de devise")
			button.config(command=choiceTp1)
			pass
		elif var == "2":
			button1.config(text="TP 2.1 - ")
			button2.config(text="TP 2.2 - ")
			button3.config(text="TP 2.3 - ")
			button4.config(text="TP 2.4 - ")
			button.config(command=choiceTp2)
			pass
		elif var == "3":
			button1.config(text="TP 3.1 - ")
			button2.config(text="TP 3.2 - ")
			button3.config(text="TP 3.3 - ")
			button4.config(text="TP 3.4 - ")
			button.config(command=choiceTp3)
			pass
		elif var == "4":
			button1.config(text="TP 4.1 - ")
			button2.config(text="TP 4.2 - ")
			button3.config(text="TP 4.3 - ")
			button4.config(text="TP 4.4 - ")
			button.config(command=choiceTp4)
			pass

	
	def choiceTp1(self):
		var = value.get()
		if var == "":
			pass
		elif var == "1":
			self.calculateFrame()
		elif var == "2":
			self.master.destroy()
		elif var == "3":
			self.master.destroy()
		elif var == "4":
			self.master.destroy()

	def choiceTp2(self):
		pass

	def choiceTp3(self):
		pass
	
	def choiceTp4(self):
		pass
		
	# bouton de sortie
	button = Button(Frame2, bg="grey", text="Séléctionner", command=choiceTp)
	button.pack()

	exitButton = Button(Frame2, bg="grey", text="Quitter", command=self.master.destroy)
	exitButton.pack()

	def calculateFrame(self):
		self.destroy()
		# frame 1
		Frame1 = Frame(self, borderwidth=2, relief=GROOVE)
		Frame1.pack(side=LEFT, padx=30, pady=30)

		# frame 2
		Frame2 = Frame(self, borderwidth=2, relief=GROOVE)
		Frame2.pack(side=LEFT, padx=10, pady=10)

		# Ajout de labels
		Label(Frame1, text="test").pack(padx=10, pady=10)
		pass

	def sumFactorialFrame(self):
		pass

	def conjugaitionFrame(self):
		pass

	def currencyConverterFrame(self):
		pass