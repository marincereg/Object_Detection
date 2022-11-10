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

import CollectImages
import LogCreator

def Collect ():
    LogCreator.Log_MSG("[HMI.py ] Collect Images call ")
    In1 = InputDirectoryName.get()
    in2 = NumberOfImages.get()
    LogCreator.Log_MSG("[HMI.py ] Collect Images parameters : InputDirectoryName =  "  +str(In1) + " and Number of images = " +str(in2))
    CollectImages.CollectImage(In1, int(in2))
    
def LabelApp ():
    LogCreator.Log_MSG("[HMI.py ] Labeling App is Starting ")
    CollectImages.StartLabelingApp()

LogCreator.SW_InRun()
LogCreator.Log_MSG("[HMI.py ] Started ")
# Create an instance of tkinter frame
win = Tk()
LogCreator.Log_MSG("[HMI.py ] Instance of Gui created ")

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

# Objects in Collect Images

Label(f1, text="Input name of direcotry :", bg="#78909c", fg="white").place(x=10, y=20)
InputDirectoryName = Entry( f1 , width= 30)
InputDirectoryName.configure(bd=5)
InputDirectoryName.place(x=180, y=20)

Label(f1, text="Input number of images :", bg="#78909c", fg="white").place(x=10, y=80)
NumberOfImages = Entry( f1, width= 10)
NumberOfImages.configure(bd=5)
NumberOfImages.place(x=180, y=80)

Label(f1, text="Create Images", bg="#78909c", fg="white").place(x=100, y=140)
Button(f1, text="Accept", command= lambda : Collect()).place(x=210, y=137)

Label(f1, text="Start App for Labeling", bg="#78909c", fg="white").place(x=10, y=230)
Button(f1, text="Start App", command= lambda : LabelApp()).place(x=160, y=229)

# Label For Train Model
label = Label(f2, text='This is a label')
label.pack(ipadx=10, ipady=10)

# Label For Phun Tab
label = Label(f3, text='This is a label')
label.pack(ipadx=10, ipady=10)

nb.pack(expand= True, fill=BOTH, padx= 5, pady=5)

win.mainloop()


