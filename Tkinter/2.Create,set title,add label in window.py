#2. Create a window and set its title
# and add a label to the window

import tkinter as tk
parent = tk.Tk()
parent.title("_Welcome to python tkinter Basic exercises_")
my_label = tk.Label(parent,text = "Label widget")
my_label.grid(column=0,row=0)
parent.mainloop()
