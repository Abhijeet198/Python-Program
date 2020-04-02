# Create a Listbox bar widgets using tkinter module

import tkinter as tk
parent = tk.Tk()
parent.geometry("250*200")
labell = tk.Label(parent,text = "A list of favorite languages...")
listbox = tk.Listbox(parent)
listbox.insert(1,"PHP")
listbox.insert(2,"Python")
listbox.insert(3,"Java")
listbox.insert(4,"C#")
labell.pack()
listbox.pack()
parent.mainloop()
