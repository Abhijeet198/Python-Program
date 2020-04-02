# Create a Text widget using tkinter module

import tkinter as tk

patrent = tk.Tk()

#Create the widget
mytext = tk.Text(parent)

#Insert a String at the beginning
mytext.insert('1.0',"-Python exercise, solution -")

#insert a string into the current text
mytext.insert('1.19','Practice,')

# delete the first and last character (including a newline character)
mytext.delete('1.0')
mytext.delete('end - 2 chars')
mytext.pack()
parent.mainloop()

