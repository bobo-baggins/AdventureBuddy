import tkinter as tk
from chunk import *

window = tk.Tk()

frame1 = tk.Frame(window, relief = tk.RAISED, borderwidth=5)
#frame2 = tk.Frame(window, relief = tk.SUNKEN, borderwidth=5, width =25, height=10)

text_B_1 = text_B("Notes")
#text_B_2 = text_B("Skills")

text_B_1.draw(frame1)
#text_B_2.draw(frame2)

frame1.pack()
#frame2.pack()

#text_B_1.fill_text(1.0,'yummy\ntummy')
#text_B_1.lock_text(frame1)

window.mainloop()
