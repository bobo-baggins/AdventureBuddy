import tkinter as tk

class Chunk:
	def __init__(self, data):
		self.ratioX = 1
		self.ratioY = 1
		self.data = data
	
	def draw(self, frame):
		print("poo")

class Words(Chunk):
	'''
	def __init__(self, text):
		super().__init__(self)
		self.text = text
	'''
	def draw(self, frame):
		self.lab = tk.Label(master=frame, text=self.data)
		self.lab.pack()

