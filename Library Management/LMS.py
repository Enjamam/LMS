from tkinter import *
from PIL import ImageTk, Image
import pymysql
import os
import sys
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk
from MainLibrarian import *
from MainAdmin import *


def liblogin():
    # Add your own database name and password here to reflect in the code
    myuser = "LMS"
    mypass = "0000"
    mydatabase="account"

    con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
    cur = con.cursor()
    cur.execute('SELECT * FROM librarian WHERE UserName = %s AND Password = %s', (user_entry.get(), password_entry.get(),))
    # Fetch one record and return result
    account = cur.fetchone()

    if account:
        root.destroy()
        Main()
        # admin()
        # messagebox.showinfo("Login System", "Logged in successfully!")
    elif user_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif password_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif user_entry.get() == "" and password_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    else:
        messagebox.showinfo("Login System", "Please enter the correct Username and Password")


def adminlogin():
    # Add your own database name and password here to reflect in the code
    myuser = "LMS"
    mypass = "0000"
    mydatabase="account"

    con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
    cur = con.cursor()
    cur.execute('SELECT * FROM admin WHERE UserName = %s AND Password = %s', (user_entry.get(), password_entry.get(),))
    # Fetch one record and return result
    account = cur.fetchone()

    if account:
        root.destroy()
        # Main()
        Main_Admin()
        # messagebox.showinfo("Login System", "Logged in successfully!")
    elif user_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif password_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif user_entry.get() == "" and password_entry.get() == "":
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    else:
        messagebox.showinfo("Login System", "Please enter the correct Username and Password")

def CommandCheck():
    if agreement.get() == "Login as Admin": adminlogin()
    else: liblogin()

def AdminOption():
    global agreement
    agreement = StringVar()

    # def agreement_changed():
       # messagebox.showinfo(title='Result', message=agreement.get())

    ttk.Checkbutton(root,
                    text = 'Login as Admin',
                    command = None,
                    variable = agreement,
                    onvalue = 'Login as Admin',
                    offvalue = 'Login as Librarian').place(x=230, y=270)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


root = Tk()
root.title("IIUC Central Library")
pathLogo = resource_path("logo.ico")
pathBG = resource_path("BG.jpg")
root.iconbitmap(pathLogo)
#img = PhotoImage('logo.png')
#root.iconphoto(True, img)
root.resizable(0, 0)
bg = Image.open(pathBG)
bg.thumbnail((600,500))
width, height = bg.size
bg = ImageTk.PhotoImage(bg)


canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')

label = Label(root, text="Login Page", height=1, width=9, font=("Georgia 26 bold"), bg='#800000', fg='white', bd=6, relief=RIDGE)
canvas.create_window(180, 40, anchor="nw", window=label)
user_label = Label(root, text="User name:", height=1, width=9, font=("Georgia 18 bold"), bg='#cb4154', fg='white', bd=2, relief=GROOVE)
canvas.create_window(75, 150, anchor="nw", window=user_label)
password_label = Label(root, text="Password:", height=1, width=9, font=("Georgia 18 bold"), bg='#cb4154', fg='white', bd=2, relief=GROOVE)
canvas.create_window(75, 210, anchor="nw", window=password_label)

user_entry = Entry(root, font=("Georgia 14"), width=19, bd=6)
user_entry.focus()
canvas.create_window(230, 150, anchor="nw", window=user_entry)
paswd = StringVar()
password_entry = Entry(root, textvar=paswd, font=("Georgia 14"), width=19, bd=6, show="*")
canvas.create_window(230, 210, anchor="nw", window=password_entry)

AdminOption()
login = Button(root, text="Log In", font=("Impact 22 bold"), width=8, height = 1, bg="#cb4154", fg='White', bd=6, relief=RAISED, command = CommandCheck)
canvas.create_window(212, 300, anchor="nw", window=login)

root.mainloop()


'''
create database Account;      
use Account;                                        
create table Librarian(UserName varchar(20) primary key, Password varchar(30));

create table Admin(UserName varchar(20) primary key, Password varchar(30));
INSERT INTO Admin (UserName, Password) values ('Emrus','2642');

INSERT INTO Librarian (UserName, Password) values ('Enjamam','1234');
'''