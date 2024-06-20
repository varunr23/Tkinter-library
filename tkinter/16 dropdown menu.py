from tkinter import *

hi=Tk()

click=StringVar()
click.set('choose')

def show():
    Label(hi,text=click.get()).pack()

#drop=OptionMenu(hi,click,'pizza','burger','fries')
#drop.pack()

list=['pizza',
      'burger',
      'fries']

drop=OptionMenu(hi,click,*list)
drop.pack()

Button(hi,text='click me!',command=show).pack()

hi.mainloop()