from tkinter import *

root=Tk()

modes=[("tayota","tayota"),
      ("hyundai","hyundai"),
      ("BMW","BMW"),
      ("maruti","maruti")]

Cars=StringVar()
Cars.set('tayota')
#a=IntVar()
#same as a.get() used for input
#a.set('app')
#for setting default value

def click(value):
    global l
    l.destroy()
    l=Label(root,text='you have chosen '+value)
    l.pack()

for text,value in modes:
    Radiobutton(root,text=text,variable=Cars,value=value).pack(anchor=W)

l=Label(root,text='')

b=Button(root,text="click me!",command=lambda:click(Cars.get()))
b.pack()
root.mainloop()