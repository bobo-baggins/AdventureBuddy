import tkinter as tk
from chunk import *

class Panel:
	def __init__(self, xs, ys):
		self.xs = xs
		self.ys = ys
		self.frame = tk.Frame(width=self.xs, height=self.ys, relief="raised", borderwidth=10)
	
	def pos(self, xp, yp):
		self.xp = xp
		self.yp = yp

	def render(self):
		self.frame.place(x=self.xp, y=self.yp)

class Sheet(Chunk):
	
	def __init__(self, data, window):
		super().__init__(data)
		self.chunks = list() #dict()
		self.chunks.append(data)
		self.window = window

	def addFrame(self, parent=None):
		if (parent == None):
			wid = self.window.winfo_screenwidth()
			hei = self.window.winfo_screenheight()
			print("dof")
		else:
			wid = parent.frame.winfo_reqwidth()
			hei = parent.frame.winfo_reqheight()
			px = parent.xp
			py = parent.yp
			print("1st")#,wid, hei)
			if wid > hei:
				wid /= 2
				px += wid
			elif hei > wid:
				hei /= 2
				py += hei
			'''
			for pair in self.chunks:
				if pair == parent:
					# pull chunk out 
					self.chunks.remove(pair)
					break
			'''
			parent.frame.destroy()
			parent.frame = tk.Frame(width=wid, height=hei, relief="raised", borderwidth=10)
			#self.chunks.append([f, None])
			
		print("now:",wid, hei)
		# use parent position to find position rather than window
		wx = self.window.winfo_reqwidth()
		wy = self.window.winfo_reqheight()
		p = Panel(wid, hei)
		p.pos(px, py)
		self.chunks.append(p)
		#f.update()

	def poo():
		print("poo")
