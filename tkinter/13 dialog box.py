from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

hi=Tk()

def open():
    global img
    lol=filedialog.askopenfilename(initialdir='',title='hehehe',filetypes=(('png files','*.png'),('all files','*.*')))
    l=Label(hi,text=lol).pack()
    img=ImageTk.PhotoImage(Image.open(lol))
    Label(hi,image=img).pack()

Button(hi,text='click to open',command=open).pack()
hi.mainloop()