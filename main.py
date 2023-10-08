import tkinter as tk
from chunk import *

window = tk.Tk()
c = Words("poo daddy")
print(c.ratioX, ",", c.ratioY)
c.draw(window)
window.mainloop()
