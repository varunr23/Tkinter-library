from tkinter import *
import sqlite3

hi=Tk()

#database
#to connect to DB
DB=sqlite3.connect('name.db')
#creating cursor
c=DB.cursor()
#creating table4
DB.execute("""CREATE TABLE NAME(
           name varchar2,
           age number,
           city varchar2);
           """)
#commiting
DB.commit()
#closing DB
DB.close()
hi.mainloop()