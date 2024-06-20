from tkinter import *

hehe=Tk()

def show():
    Label(hehe,text=var.get() +' '+ var1.get()).pack()

var=StringVar()
var1=StringVar()
#var.set('on')
c=Checkbutton(hehe,text='anything',variable=var,onvalue='on',offvalue='off')
c1=Checkbutton(hehe,text='i dont know',variable=var1,onvalue='ok',offvalue='not ok')
c1.pack()
c1.deselect()
c.pack()
c.deselect()

Button(hehe,text='click to show selection',command=show).pack()

hehe.mainloop()