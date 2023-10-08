import tkinter as tk

class Chunk:
	def __init__(self, data):
		self.ratioX = 1
		self.ratioY = 1
		self.data = data
	
	def draw(self, frame):
		print("poo")

class text_B(Chunk):
	def draw(self, frame):
	# Creates title label using "data" and an empty multi-line text entry box
		self.title = tk.Label(
			master=frame,
			text=self.data,
			height = 5,
			width = 25)

		self.text_box = tk.Text(
			master=frame,
			height = 25,
			width = 125)

		self.title.pack()
		self.text_box.pack(fill=tk.BOTH, expand=True)

	def hide_title(self):	
		self.title.forget()

	def fill_text(self,cords, words):	
		self.text_box.insert(str(cords), str(words))

	def lock_text(self, frame):
		#Grabs text from the text box starting at coloumn at 1 letter 0
		self.wordss = self.text_box.get("1.0", tk.END)
		self.text_box.forget()
		#Puts text grabbed into a label
		self.text_box_L = tk.Label(master=frame,text=self.wordss)
		self.text_box_L.pack()

		