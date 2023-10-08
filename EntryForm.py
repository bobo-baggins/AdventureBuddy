import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

labels = ["First Name:", "Last Name:", "Address Line 1:", "Address Line 2:", "City", "State/Province", "Postal Code", "County"]

form = tk.Frame(relief=tk.RAISED, borderwidth=1)
form.pack()

for i in range(8):
    label = tk.Label(master=form, text=labels[i])
    label.grid(row=i, column=0, sticky = "e")
    entry = tk.Entry(master=form )
    entry.grid(row=i, column=1, sticky="e")

btn = tk.Frame()
btn.pack()

submit = tk.Button(master=btn, text = "Submit")
submit.pack(side=tk.RIGHT)

clear = tk.Button(master=btn, text = "Clear")
clear.pack(side=tk.RIGHT)

window.mainloop()