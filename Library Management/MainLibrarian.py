from tkinter import *
import time
import os
import sys
from PIL import ImageTk,Image
from MainBook import *
from MainStudent import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)

def Main():
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

    Canvas1 = Canvas(root)

    Canvas1.create_image(0, 0, image=img, anchor='nw')
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=False, fill=BOTH)

    ###########################
    headingFrame = Frame(root,bg="#3E9D83",bd=10, relief=GROOVE)
    headingFrame.place(relx=0.325,rely=0.25,relwidth=0.35,relheight=0.15)

    label = Label(headingFrame, font=("DS-Digital", 36, 'bold'), bg="black", fg="green", bd=5, relief=RIDGE)
    label.place(relx=0,rely=0, relwidth=1, relheight=1)
    #label.grid(row=0, column=1)

    def dclock():
        time_live = time.strftime("%H:%M:%S")
        label.config(text=time_live)
        label.after(200, dclock)

    dclock()
    #############################

    def Stu():
         root.destroy()
         Students()

    def Book():
         root.destroy()
         Books()

    headingFrame1 = Frame(root,bg="#3E9D83",bd=6, relief=GROOVE)
    headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.18)

    headingLabel = Label(headingFrame1, text="Welcome to \n IIUC Central Library", bg='#336372', fg='#FDFDFC', font=('Georgia Bold', 18), bd=8, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Student Menu",bg='teal', fg='white', font=('Georgia Bold', 18), bd=10, command=Stu)
    btn1.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.15)
        
    btn2 = Button(root,text="Book Menu",bg='teal', fg='white', font=('Georgia Bold', 18), bd=10, command=Book)
    btn2.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.15)

    btn3 = Button(root,text="Exit",bg='teal', fg='white', font=('Georgia Bold', 18), bd=10, command=root.destroy)
    btn3.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.15)
        
    root.mainloop()

# Main()