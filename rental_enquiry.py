
from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        
        self.heading = Label(master, text="Bookings ",  fg='grey', font=('arial 40 bold'))
        self.heading.place(x=150, y=20)

       
        self.name = Label(master, text="Enter Owner's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=100)

        
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=92)

        
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=132)
    

        
        self.uname = Label(self.master, text="Owner's Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=160)

        self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=280)

        self.utime = Label(self.master, text="Entry Time", font=('arial 18 bold'))
        self.utime.place(x=0, y=320)

        self.udate = Label(self.master, text="Entry Time", font=('arial 18 bold'))
        self.udate.place(x=0, y=320)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphone.place(x=0, y=360)

        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=170)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=290)
        self.ent2.insert(END, str(self.location))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=330)
        self.ent4.insert(END, str(self.time))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=330)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=370)
        self.ent6.insert(END, str(self.phone))

        
        self.update = Button(self.master, text="Update?", width=20, height=2,fg='white', bg='black', command=self.update_db)
        self.update.place(x=400, y=410)


root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()