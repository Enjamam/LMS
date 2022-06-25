from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import sys
import os

# Add your own database name and password here to reflect in the code
mypass = "0000"
mydatabase = "student"

con = pymysql.connect(host="localhost", user="LMS", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
studentTable = "students"


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def Viewstu():
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
    Canvas1.config(bg='#F5F5F5')
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5, relief=GROOVE)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Student", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='Lavender', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5) 
    y = 0.25

    Label(labelFrame, text="%+7s%+40s"%('ID', 'Student Name'), font=('Georgia', 10, 'bold'), bg='Lavender', fg='black').place(relx=0.23, rely=0.1)
    Label(labelFrame, text="-------------------------------------------------", bg='Lavender',fg='black').place(relx=0.20, rely=0.17)
    getStudents = "select * from " + studentTable
    try:
        cur.execute(getStudents)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%+10s"%(i[0], i[1]), font=('Consolas', 12, 'bold'), bg='Lavender', fg='black').place(relx=0.23, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="QUIT", font=("Georgia 15 bold"), bg='#27282C', fg='#F41A05', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

#Viewstu()