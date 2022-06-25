import imp
from tkinter import *
from PIL import ImageTk,Image
import pymysql
import sys
import os
from tkinter import messagebox
from ViewStudents import *
from AddStudent import *
from DeleteStudent import *
from UpdateStudent import *


# Add your own database name and password here to reflect in the code
myuser = "LMS"
mypass = "0000"
mydatabase= "book"

con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
cur = con.cursor()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def Students():
    root = Tk()
    root.title("IIUC Central Library")
    pathLogo = resource_path("logo.ico")
    pathBG = resource_path("Lib2.jpg")
    root.iconbitmap(pathLogo)
    #img = PhotoImage('logo.png')
    #root.iconphoto(True, img)
    #root.minsize(width=400,height=400)
    #root.maxsize(width=400,height=400)
    root.geometry("600x500")
    root.resizable(0,0)

    bg = Image.open(pathBG)
    bg.thumbnail((600,500))
    #width, height = bg.size
    newImageSizeWidth = 600
    newImageSizeHeight = 500
    img = ImageTk.PhotoImage(bg)

    #def backtomain():
         #import MainMenu
         #root.destroy()
         #Main()

    Canvas1 = Canvas(root)
    Canvas1.create_image(0, 0, image=img, anchor='nw')
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=False, fill=BOTH)

    headingFrame1 = Frame(root,bg="#3E9D83",bd=6, relief=GROOVE)
    headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.18)

    headingLabel = Label(headingFrame1, text="Welcome to \n IIUC Central Library", bg='#336372', fg='#FDFDFC', font=('Georgia Bold', 18), bd=8, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Students Details",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command=addstudents)
    btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.12)

    btn2 = Button(root,text="Edit Student Details",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command=UpdateStu)
    btn2.place(relx=0.28,rely=0.46, relwidth=0.45,relheight=0.12)

    btn3 = Button(root,text="Delete Student",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command=deletestu)
    btn3.place(relx=0.28,rely=0.57, relwidth=0.45,relheight=0.12)

    btn4 = Button(root,text="View Students List",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command=Viewstu)
    btn4.place(relx=0.28,rely=0.68, relwidth=0.45,relheight=0.12)

    btn5 = Button(root,text="Exit",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command = root.destroy)
    btn5.place(relx=0.28,rely=0.79, relwidth=0.45,relheight=0.12)

    root.mainloop()