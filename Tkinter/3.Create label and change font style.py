# Create a label and change the label font style using
# using tkinter module

import tkinter as tk
parent = tk.Tk()
parent.title("_Welcome to Python tkinter Basic exercise-")
my_label = tk.Label(parent,text="Hello", font=("Arial Bold,70"))
my_label.grid(column=0, row=0)
parent.mainloop()
