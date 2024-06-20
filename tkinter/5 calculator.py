from tkinter import *

A=Tk()

A.title('Calculator')

def click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))

def add():
    global tree
    global first_num
    tree='add'
    first_num=entry.get()
    entry.delete(0,END)

def sub():
    global tree
    global first_num
    tree='sub'
    first_num=entry.get()
    entry.delete(0,END)

def mul():
    global tree
    global first_num
    tree='mul'
    first_num=entry.get()
    entry.delete(0,END)

def div():
    global tree
    global first_num
    tree='div'
    first_num=entry.get()
    entry.delete(0,END)

def equal():
    second_num=entry.get()
    entry.delete(0,END)

    if tree=='add':
        entry.insert(0,float(first_num)+float(second_num))

    if tree=='sub':
        entry.insert(0,int(first_num)-int(second_num))

    if tree=='mul':
        entry.insert(0,int(first_num)*int(second_num))

    if tree=='div':
        entry.insert(0,int(first_num)/int(second_num))
                         

def clear():
    entry.delete(0,END)

entry=Entry(A,width=35,borderwidth=5)

button_1=Button(A,text="1",padx=25,pady=25,command=lambda:click(1))
button_2=Button(A,text="2",padx=25,pady=25,command=lambda:click(2))
button_3=Button(A,text="3",padx=25,pady=25,command=lambda:click(3))
button_4=Button(A,text="4",padx=25,pady=25,command=lambda:click(4))
button_5=Button(A,text="5",padx=25,pady=25,command=lambda:click(5))
button_6=Button(A,text="6",padx=25,pady=25,command=lambda:click(6))
button_7=Button(A,text="7",padx=25,pady=25,command=lambda:click(7))
button_8=Button(A,text="8",padx=25,pady=25,command=lambda:click(8))
button_9=Button(A,text="9",padx=25,pady=25,command=lambda:click(9))
button_0=Button(A,text="0",padx=25,pady=25,command=lambda:click(0))

button_add=Button(A,text="+",padx=25,pady=25,command=add)
button_sub=Button(A,text="-",padx=25,pady=25,command=sub)
button_mul=Button(A,text="x",padx=25,pady=25,command=mul)
button_div=Button(A,text="/",padx=25,pady=25,command=div)

button_equal=Button(A,text="=",padx=25,pady=25,command=equal)
button_clear=Button(A,text="clear",padx=25,pady=25,command=clear)


entry.grid(row=0,column=0,columnspan=3)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)

button_div.grid(row=5,column=0)
button_mul.grid(row=5,column=1)
button_equal.grid(row=5,column=2)
button_clear.grid(row=6,column=0)


A.mainloop()