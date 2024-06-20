from tkinter import *

root=Tk()

frame=LabelFrame(root,text="my frame",padx=50,pady=5)
frame.pack(padx=10,pady=10)
b=Button(frame,text="useless")
b.grid(row=0,column=0)
b=Button(frame,text="useless")
b.grid(row=0,column=1)
root.mainloop()