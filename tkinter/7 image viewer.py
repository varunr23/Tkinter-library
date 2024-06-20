from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('image viewer')

img_1=ImageTk.PhotoImage(Image.open('images/1.jpg'))
img_2=ImageTk.PhotoImage(Image.open('images/2.jpg'))
img_3=ImageTk.PhotoImage(Image.open('images/3.jpg'))
img_4=ImageTk.PhotoImage(Image.open('images/4.jpg'))
image_list=[img_1,img_2,img_3,img_4]

status=Label(root,text='Image 1 of 4',bd=1,relief=SUNKEN,anchor=E).grid(row=2,column=0,columnspan=3,sticky=W+E)

def forwardd(number):
    global label
    label.grid_forget()
    #or label.destroy()
    label=Label(root,image=image_list[number])
    label.grid(row=0,column=0,columnspan=3)
    forward=Button(root,text='>>',command=lambda:forwardd(number+1))
    back=Button(root,text='<<',command=lambda:backk(number-1)).grid(row=1,column=0)
    if number==3:
        forward=Button(root,text='>>',state=DISABLED)
    forward.grid(row=1,column=2)
    status=Label(root,text='Image '+str(number+1)+' of 4',bd=1,relief=SUNKEN,anchor=E).grid(row=2,column=0,columnspan=3,sticky=W+E)


def backk(number):
    global label
    label.destroy()
    label=Label(root,image=image_list[number])
    label.grid(row=0,column=0,columnspan=3)
    forward=Button(root,text='>>',command=lambda:forwardd(number+1)).grid(row=1,column=2)
    back=Button(root,text='<<',command=lambda:backk(number-1))
    if number==0:
        back=Button(root,text='<<',state=DISABLED)
    back.grid(row=1,column=0)
    status=Label(root,text='Image '+str(number+1)+' of 4',bd=1,relief=SUNKEN,anchor=E).grid(row=2,column=0,columnspan=3,sticky=W+E)

label=Label(root,image=image_list[0])
label.grid(row=0,column=0,columnspan=3)

forward=Button(root,text='>>',command=lambda:forwardd(1)).grid(row=1,column=2)
back=Button(root,text='<<',state=DISABLED).grid(row=1,column=0)
button_quit=Button(root,text="exit",command=root.quit).grid(row=1,column=1,pady=10)


root.mainloop()