# Create a window and diable to resize the window
# using tkinter module

import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to python tkinter Basic exercises-")

# Disable resizing the GUI
parent.resizable(0,0)
parent.mainloop()

