from tkinter import *
from tkinter import messagebox

root=Tk()

def popup():
    #showinfo , showerror, showwarning, askquestion, askokcancel, askyesno ,askretrycancel ,askyesnocancel
    response=messagebox.askyesno("this is a popup","i said don't click")
    Label(root,text=response).pack()

Button(root,text="don't click",command=popup).pack()

root.mainloop()