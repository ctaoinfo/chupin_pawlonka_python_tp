from tkinter import *
import tkinter as tk

class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.value = StringVar()
		self.showMenu()

	def choiceTp(self):
		print(self.value)
		var = self.value
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

	
	def choiceTp1(self):
		var = self.value
		if var == "":
			pass
		elif var == "1":
			self.calculateFrame()
		elif var == "2":
			self.destroy()
		elif var == "3":
			self.destroy()
		elif var == "4":
			self.destroy()

	def choiceTp2(self):
		pass

	def choiceTp3(self):
		pass
	
	def choiceTp4(self):
		pass
		
	

	def calculateFrame(self):
		self.destroy()
		# frame 1
		self.Frame1 = tk.Frame(self, borderwidth=2, relief=GROOVE)
		self.Frame1.pack(side=LEFT, padx=30, pady=30)

		# frame 2
		self.Frame2 = tk.Frame(self, borderwidth=2, relief=GROOVE)
		self.Frame2.pack(side=LEFT, padx=10, pady=10)

		# Ajout de labels
		self.Label(self.Frame1, text="test").pack(padx=10, pady=10)

	def sumFactorialFrame(self):
		pass

	def conjugaitionFrame(self):
		pass

	def currencyConverterFrame(self):
		pass

	def showMenu(self):
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

if __name__ == "__main__":
	app = App()
	app.title("Test")
	app.mainloop()

