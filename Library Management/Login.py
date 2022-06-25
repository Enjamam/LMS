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


def btn_clicked():
    print("Button Clicked")
    print(user_entry.get())


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
    if agreement.get() == "Login as Librarian": liblogin()

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
                    offvalue = 'Login as Librarian').place(x=348, y=338)

    ttk.Checkbutton(root,
                    text='Login as Librarian',
                    command=None,
                    variable=agreement,
                    onvalue='Login as Librarian',
                    offvalue='Login as Admin').place(x=348, y=355)


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
root.iconbitmap('logo.ico')
root.geometry("600x500")
root.configure(bg = "#ffffff")
canvas = Canvas(
    root,
    bg = "#ffffff",
    height = 500,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    193.5, 236.5,
    image=background_img)

AdminOption()
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = CommandCheck,
    relief = "flat")

b0.place(
    x = 399, y = 377,
    width = 95,
    height = 30)

user_entry_img = PhotoImage(file = f"img_textBox0.png")
user_entry_bg = canvas.create_image(
    446.0, 251.5,
    image = user_entry_img)

user_entry = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

user_entry.place(
    x = 348.0, y = 238,
    width = 196.0,
    height = 25)

password_entry_img = PhotoImage(file = f"img_textBox1.png")
password_entry_bg = canvas.create_image(
    446.0, 318.5,
    image = password_entry_img)

password_entry = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

password_entry.place(
    x = 348.0, y = 305,
    width = 196.0,
    height = 25)

root.resizable(False, False)
root.mainloop()
