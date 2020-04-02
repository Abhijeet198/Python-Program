# Create a  Scrolled Text widgets using tkinter module

import tkinter as tk
import tkinter.scrolledtext as tkst
parent = tk.Tk()
parent.title("ScrolledText")
parent.geometry('350*200')
txt = tkst.ScrolledText(parent, width=40, height=10)
txt.grid(column=0,row=0)
parent.mainloop()
