import tkinter as tk

gui = tk.Tk()

gui.geometry("300x300")

def getEntry():
    res = MyEntry.get()
    print(res)

MyEntry = tk.Entry(gui,width = 40 )
MyEntry.pack()

btn = tk.Button(gui, text="Try" , command = lambda : getEntry())
btn.pack()

gui.mainloop()