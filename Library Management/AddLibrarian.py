from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import sys
import os


def addlib():
    # Add your own database name and password here to reflect in the code
    myuser = "LMS"
    mypass = "0000"
    mydatabase= "account"

    con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
    cur = con.cursor()

    fullnam = librarianInfo1.get()
    usernam = librarianInfo2.get()
    userpass = librarianInfo3.get()
    librarian = "librarian"
    
    insertLib = "insert into "+librarian+" values('"+fullnam+"','"+usernam+"','"+userpass+"')"
    try:
        cur.execute(insertLib)
        con.commit()
        messagebox.showinfo('Success',"Librarian added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    print(fullnam)
    print(usernam)
    print(userpass)

    root.destroy()


def checkid():
    if librarianInfo1.get() == "" and librarianInfo2.get() == "" and librarianInfo3.get() == "":
        messagebox.showinfo("Login System", "Please enter the Full Name, Username and Password")
    elif librarianInfo1.get() == "" and librarianInfo2.get() == "":
        messagebox.showinfo("Login System", "Please enter the Full Name and Username")
    elif librarianInfo1.get() == "" and librarianInfo3.get() == "":
        messagebox.showinfo("Login System", "Please enter the Full Name and Password")
    elif librarianInfo2.get() == "" and librarianInfo3.get() == "":
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    elif librarianInfo1.get() == "":
        messagebox.showinfo("Login System", "Please enter the Full Name")
    elif librarianInfo2.get() == "":
        messagebox.showinfo("Login System", "Please enter the User Name")
    elif librarianInfo3.get() == "":
        messagebox.showinfo("Login System", "Please enter the Password")
    else:
        addlib()
        # root.destroy()
        # import main
        # messagebox.showinfo("Login System", "Successfully Loged in")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def addlibri():
    global librarianInfo1, librarianInfo2, librarianInfo3, Canvas1, con, cur, studentTable, root

    root = Tk()
    root.title("IIUC Central Library")
    pathLogo = resource_path("logo.ico")
    root.iconbitmap(pathLogo)
    # img = PhotoImage('logo.png')
    # root.iconphoto(True, img)
    root.resizable(0, 0)
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#C0C0C0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5, relief=GROOVE)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Add Librarian", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='#A9A9A9', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # Full Name
    lb1 = Label(labelFrame, text="Full Name : ", font=("Georgia 10 bold"), bg='#A9A9A9', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    librarianInfo1 = Entry(labelFrame, font=("Georgia 8 bold"), bd=4)
    librarianInfo1.focus()
    librarianInfo1.place(relx=0.3, rely=0.2, relwidth=0.64, relheight=0.10)

    # User Name
    lb2 = Label(labelFrame, text="User Name : ", font=("Georgia 10 bold"), bg='#A9A9A9', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    librarianInfo2 = Entry(labelFrame, font=("Georgia 8 bold"), bd=4)
    librarianInfo2.place(relx=0.3, rely=0.35, relwidth=0.64, relheight=0.10)

    # PasswordGeorgia
    lb3 = Label(labelFrame, text="Password: ", font=("Georgia 8 bold"), bg='#A9A9A9', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    librarianInfo3 = Entry(labelFrame, font=("Georgia 8 bold"), bd=4, show="*")
    librarianInfo3.place(relx=0.3, rely=0.50, relwidth=0.64, relheight=0.10)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5, command=checkid)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5, command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

#addlibri()

'''
create database account;      
use account;                                        
create table librarian(FullName varchar(20) primary key, UserName varchar(50), Password varchar(50));
'''