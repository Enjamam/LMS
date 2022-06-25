from audioop import add
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import sys
import os


def studentRegister():
    id = studentInfo1.get()
    name = studentInfo2.get()

    insertstudents = "insert into " + studentTable + " values('" + id + "','" + name + "')"
    try:
        cur.execute(insertstudents)
        con.commit()
        messagebox.showinfo('Success', "Student added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(id)
    print(name)

    root.destroy()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def addstudents():
    global studentInfo1, studentInfo2, studentInfo3,  Canvas1, con, cur, studentTable, root

    root = Tk()
    root.title("IIUC Central Library")
    pathLogo = resource_path("logo.ico")
    root.iconbitmap(pathLogo)
    # img = PhotoImage('logo.png')
    # root.iconphoto(True, img)
    root.resizable(0, 0)
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "0000"
    mydatabase = "student"

    con = pymysql.connect(host="localhost", user="LMS", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    studentTable = "students"  # Student  Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#C0C0C0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5, relief=GROOVE)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Add Student", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='#A9A9A9', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # Student ID
    lb1 = Label(labelFrame, text="Student ID : ", font=("Georgia 10 bold"), bg='#082E9A', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    studentInfo1 = Entry(labelFrame, font=("Georgia 10"), bd=4)
    studentInfo1.focus()
    studentInfo1.place(relx=0.3, rely=0.2, relwidth=0.64, relheight=0.10)

    # Title
    lb2 = Label(labelFrame, text=" Full Name : ", font=("Georgia 10 bold"), bg='#082E9A', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    studentInfo2 = Entry(labelFrame, font=("Georgia 10"), bd=4)
    studentInfo2.place(relx=0.3, rely=0.35, relwidth=0.64, relheight=0.10)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5, command=studentRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5, command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

#addstudents()

'''
create database Student;      
use Student;                                        
create table students(ID varchar(20) primary key, Name varchar(50));
'''