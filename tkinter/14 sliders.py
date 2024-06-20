from tkinter import *

hi=Tk()
hi.geometry('500x500')

'''def resize(var):
    hi.geometry(str(horizontal.get())+'x'+str(vertical.get()))

vertical=Scale(hi,from_=100, to=1000,command=resize)
vertical.pack()
horizontal=Scale(hi,from_=100, to=1000,orient=HORIZONTAL,command=resize)
horizontal.pack()'''

def resize():
    hi.geometry(str(horizontal.get())+'x'+str(vertical.get()))

vertical=Scale(hi,from_=100, to=1000)
vertical.pack()
horizontal=Scale(hi,from_=100, to=1000,orient=HORIZONTAL)
horizontal.pack()

Button(hi,text='click for resize',command=resize).pack()

hi.mainloop()