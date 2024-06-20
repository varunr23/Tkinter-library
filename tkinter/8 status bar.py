from tkinter import *

root=Tk()
button=Button(root,text="useless").grid(row=0,column=0,pady=10)
button=Button(root,text="useless").grid(row=0,column=1,pady=10)
status=Label(root,text='Image 1 of 4',padx=10,bd=1,relief=SUNKEN,anchor=E).grid(row=1,column=0,columnspan=2,sticky=W+E)
#dont use padx or pady while using sticky

root.mainloop()