from tkinter import *
from turtle import back
from PIL import ImageTk,Image
import pymysql
import os
import sys
from tkinter import messagebox
from AddBook import *
from UpdateBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *


# Add your own database name and password here to reflect in the code
myuser = "LMS"
mypass = "0000"
mydatabase = "book"

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


def Books():
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

    def GoToLib():
        root.destroy()
        import MainLibrarian

    Canvas1 = Canvas(root)
    Canvas1.create_image(0, 0, image=img, anchor='nw')
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=False, fill=BOTH)

    headingFrame1 = Frame(root,bg="#3E9D83",bd=6)
    headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \n IIUC Central Library", bg='#336372', fg='#FDFDFC', font=('Georgia Bold', 18), relief=RAISED)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command = addBook)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.092)

    btn7 = Button(root,text="Edit Book Details",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command = Update)
    btn7.place(relx=0.28,rely=0.39, relwidth=0.45,relheight=0.092)
        
    btn2 = Button(root,text="Delete Book",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command = delete)
    btn2.place(relx=0.28,rely=0.48, relwidth=0.45,relheight=0.092)
        
    btn3 = Button(root,text="View Book List",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command=View)
    btn3.place(relx=0.28,rely=0.57, relwidth=0.45,relheight=0.092)
        
    btn4 = Button(root,text="Issue Book to Student",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command = issueBook)
    btn4.place(relx=0.28,rely=0.66, relwidth=0.45,relheight=0.092)
        
    btn5 = Button(root,text="Return Book",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command = returnBook)
    btn5.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.092)

    btn6 = Button(root,text="Exit",bg='teal', fg='white', font=('Georgia Bold', 10), bd=10, command = root.destroy)
    btn6.place(relx=0.28,rely=0.84, relwidth=0.45,relheight=0.092)

    root.mainloop()

#Books()