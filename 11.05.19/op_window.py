from tkinter import *

def open_window():
    top=Toplevel()

root=Tk()
button=Button(root,text="Open Window" , command=open_window)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()