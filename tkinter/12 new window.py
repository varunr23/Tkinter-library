from tkinter import *
from PIL import ImageTk,Image

hello=Tk()
hello.title('original')


def open():
    global img
    top=Toplevel()
    top.title('new window')
    l=Label(top,text='hello').pack()
    img=ImageTk.PhotoImage(Image.open('images/1.jpg'))
    l1=Label(top,image=img).pack()
    Button(top,text='close',command=top.destroy).pack()

b=Button(hello,text="click to open image",command=open).pack()

hello.mainloop()