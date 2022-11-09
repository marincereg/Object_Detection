# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:02:14 2022

@author: marin
"""
"""
GUI


root = tk.Tk()
root.geometry("400x400")
root.title('Object Detection')
root.config(bg='#78909c')
"""
# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("500x400")
win.config(bg='#78909c')
win.title('Object Detection')

# Create an instance of ttk style
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="teal")
s.map("TNotebook", background= [("selected", "teal")])

# Create a Notebook widget
nb = ttk.Notebook(win)

# Add a frame for adding a new tab
f1= ttk.Frame(nb)
f2 = ttk.Frame(nb)
f3 = ttk.Frame(nb)

# Adding the Tab Name
nb.add(f1, text= 'Collect Images')
nb.add(f2, text= "Train Model")
nb.add(f3, text= "Phun Tab")

nb.pack(expand= True, fill=BOTH, padx= 5, pady=5)
win.mainloop()


