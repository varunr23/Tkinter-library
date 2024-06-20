from tkinter import *
import sqlite3

hi=Tk()

#submit function
def submit():
    #to connect to DB
    DB=sqlite3.connect('name.db')
    #creating cursor
    c=DB.cursor()
    #executing
    c.execute("INSERT INTO name values(:name,:age,:city);",
              {
              'name':name.get(),
              'age':age.get(),
              'city':city.get()
              })
    #commiting
    DB.commit()
    #closing DB
    DB.close()
    #clearing
    name.delete(0,END)
    age.delete(0,END)
    city.delete(0,END)

#show function
def show(e):
    #to connect to DB
    DB=sqlite3.connect('name.db')
    #creating cursor
    c=DB.cursor()
    #executing
    if e==0:
        c.execute('select *,oid from name;')
        record=c.fetchall()
    if e==1:
        c.execute('select *,oid from name where oid='+de.get())
        record=c.fetchall()
    #printing the records 
    frame2.grid(row=0,column=1,ipadx=100,ipady=118)
    re=''
    for i in record:
            re+=str(i[0])+' '+str(i[1])+' '+str(i[2])+' '+str(i[3])+'\n'
    global l4
    l4.destroy()
    l4=Label(frame2,text=re)
    l4.grid(row=0,column=0,columnspan=2)
    #commiting
    DB.commit()
    #closing DB
    DB.close()
    #clearing
    de.delete(0,END)

#delete function
def dele():
    #to connect to DB
    DB=sqlite3.connect('name.db')
    #creating cursor
    c=DB.cursor()
    #executing
    c.execute("delete from name where oid="+de.get())
    #commiting
    DB.commit()
    #closing DB
    DB.close()
    #clearing
    de.delete(0,END)

#update function
def edi():
    global name1
    global age1
    global city1
    global de
    #to connect to DB
    DB=sqlite3.connect('name.db')
    #creating cursor
    c=DB.cursor()
    #executing
    c.execute("update name set name=:1,age=:2,city=:3 where oid=:4",
              {
                   '1':name1.get(),
                   '2':age1.get(),
                   '3':city1.get(),
                   '4':de.get()
              })
    #commiting
    DB.commit()
    #closing DB
    DB.close()
    #clearing
    name1.delete(0,END)
    age1.delete(0,END)
    city1.delete(0,END)
    de.delete(0,END)
     
#edit function
def edith():
    global name1
    global age1
    global city1
    edit=Toplevel()
    edit.title('Edit Window')

    l11=Label(edit,text='Enter Name:')
    l21=Label(edit,text='Enter Age:')
    l31=Label(edit,text='Enter City:')
    name1=Entry(edit,width=30)
    age1=Entry(edit,width=30)
    city1=Entry(edit,width=30)
    l11.grid(row=0,column=0,sticky=W,padx=10,pady=10)
    name1.grid(row=0,column=1,padx=10,pady=10)
    l21.grid(row=1,column=0,sticky=W,padx=10)
    age1.grid(row=1,column=1)
    l31.grid(row=2,column=0,sticky=W,padx=10,pady=10)
    city1.grid(row=2,column=1,padx=10,pady=10)

    #edit button
    b5=Button(edit,text='EDIT',width=30,command=edi)
    b5.grid(row=3,column=0,columnspan=2)

    #close button#
    b6=Button(edit,text='CLOSE',command=edit.destroy,width=30)
    b6.grid(row=4,column=0,columnspan=2)

    #to connect to DB
    DB=sqlite3.connect('name.db')
    #creating cursor
    c=DB.cursor()
    #executing
    c.execute("select * from name where oid="+de.get())
    record=c.fetchall()
    name1.insert(0,record[0][0])
    age1.insert(0,record[0][1])
    city1.insert(0,record[0][2])
    
    #commiting
    DB.commit()
    #closing DB
    DB.close()
    
#frames
frame1=LabelFrame(hi)
frame1.grid(row=0,column=0)
frame2=LabelFrame(hi)

#labels and textboxes
l1=Label(frame1,text='Enter Name:')
l2=Label(frame1,text='Enter Age:')
l3=Label(frame1,text='Enter City:')
name=Entry(frame1,width=30)
age=Entry(frame1,width=30)
city=Entry(frame1,width=30)
l1.grid(row=0,column=0,sticky=W,padx=10,pady=10)
name.grid(row=0,column=1,padx=10,pady=10)
l2.grid(row=1,column=0,sticky=W,padx=10)
age.grid(row=1,column=1)
l3.grid(row=2,column=0,sticky=W,padx=10,pady=10)
city.grid(row=2,column=1,padx=10,pady=10)
l4=Label(frame2)
l5=Label(frame1,text='Enter OID:')
l5.grid(row=5,column=0,sticky=W,padx=10,pady=10)
de=Entry(frame1,width=30)
de.grid(row=5,column=1,padx=10,pady=10)

#submit button
b=Button(frame1,text='Submit',width=35,command=submit)
b.grid(row=3,column=0,columnspan=2,padx=10,pady=(10,5))

#show button
b1=Button(frame1,text='Show All Records',width=35,command=lambda:show(0))
b1.grid(row=4,column=0,columnspan=2,padx=10,pady=(5,10))

b3=Button(frame1,text='Show Record',width=35,command=lambda:show(1))
b3.grid(row=7,column=0,columnspan=2)

#delete button
b2=Button(frame1,text='Delete Record',width=35,command=dele)
b2.grid(row=6,column=0,columnspan=2,padx=10,pady=10)

#edit button
b4=Button(frame1,text='Edit Record',width=35,command=edith)
b4.grid(row=8,column=0,columnspan=2,padx=10,pady=10)

hi.mainloop()