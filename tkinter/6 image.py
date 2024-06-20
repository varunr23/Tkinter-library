from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title('image viewer')
root.iconbitmap('d:/The.ico')

img_1=ImageTk.PhotoImage(Image.open('1.jpg'))


label=Label(image=img)
label.pack()


button_quit=Button(root,text="exit",command=root.quit)

button_quit.pack()



root.mainloop()