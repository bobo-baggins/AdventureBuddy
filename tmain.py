import tkinter as tk
from chunk import *
from sheet import *

window = tk.Tk()
wx = window.winfo_screenwidth()
wy = window.winfo_screenheight()
window.geometry(str(wx)+"x"+str(wy))
print(wx, wy)

sheet = Panel(wx*0.6, wy)
sheet.pos(wx*0.2,0)
s = Sheet(sheet, window)
s.addFrame(s.chunks[0])#sheet.f)
'''
s.addFrame(s.chunks[1])
s.addFrame(s.chunks[2])
s.addFrame(s.chunks[0])
'''
tb = text_B("POO")
tb.draw(s.chunks[0].frame)
for sheet in s.chunks:
	sheet.render()

#s.addFrame()
'''
f = tk.Frame(master=window,relief="raised", borderwidth=2, width=150, height=150)
s.chunks[f] = None
#s.chunks.keys()[0].pack()
for fr in s.chunks.keys():
	fr.pack()
'''
#s.chunks[0][0].pack()
#s.addFrame(s.chunks[0][0])
#s.addFrame(s.chunks[1][0])
'''
for pair in s.chunks:
	print(pair[0].winfo_reqwidth(), ",", pair[0].winfo_reqheight())
	pair[0].place(x=0,y=0)
'''
'''
s.chunks[0][0].pack()
s.chunks[1][0].pack()
'''
window.mainloop()
