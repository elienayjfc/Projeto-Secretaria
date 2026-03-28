from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=200)
frm.grid()
ttk.Label(frm, text= "Teste").grid(column=0, row=0)
ttk.Button(frm, text= "cancel", command=root.destroy).grid(column=1,row=0)
root.mainloop()