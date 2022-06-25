from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import sys
import os

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    publisher = bookInfo5.get()
    genre = bookInfo6.get()
    #status = status.lower()
    
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+publisher+"','"+genre+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(publisher)
    print(genre)
    print(status)

    root.destroy()
    
def setAI():
    global status
    status = bookInfo4.get()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("IIUC Central Library")
    pathLogo = resource_path("logo.ico")
    root.iconbitmap(pathLogo)
    #img = PhotoImage('logo.png')
    #root.iconphoto(True, img)
    root.resizable(0,0)
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    myuser = "LMS"
    mypass = "0000"
    mydatabase="book"

    con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg='#F5F5F5')
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5, relief=GROOVE)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Add Book", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='Lavender', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", font=("Georgia 8 bold"), bg='Lavender', fg='black')
    lb1.place(relx=0.08,rely=0.1, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame, font=("Georgia 8"), bd=3)
    bookInfo1.focus()
    bookInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", font=("Georgia 8 bold"), bg='Lavender', fg='black')
    lb2.place(relx=0.08,rely=0.23, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame, font=("Georgia 8"), bd=3)
    bookInfo2.place(relx=0.3,rely=0.23, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", font=("Georgia 8 bold"), bg='Lavender', fg='black')
    lb3.place(relx=0.08,rely=0.36, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame, font=("Georgia 8"), bd=3)
    bookInfo3.place(relx=0.3,rely=0.36, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Quantity : ", font=("Georgia 8 bold"), bg='Lavender', fg='black')
    lb4.place(relx=0.08,rely=0.75, relheight=0.08)

    bookInfo4 = Entry(labelFrame, font=("Georgia 8"), bd=3)
    bookInfo4.place(relx=0.3,rely=0.75, relwidth=0.62, relheight=0.08)

    # Book Publisher
    lb5 = Label(labelFrame,text="Publisher : ", font=("Georgia 8 bold"), bg='Lavender', fg='black')
    lb5.place(relx=0.08,rely=0.62, relheight=0.08)

    bookInfo5 = Entry(labelFrame, font=("Georgia 8"), bd=3)
    bookInfo5.place(relx=0.3,rely=0.62, relwidth=0.62, relheight=0.08)

    # Book Genre
    lb6 = Label(labelFrame, text="Genre : ", font=("Georgia 8 bold"), bg='Lavender', fg='black')
    lb6.place(relx=0.08, rely=0.49, relheight=0.08)

    bookInfo6 = Entry(labelFrame, font=("Georgia 8"), bd=3)
    bookInfo6.place(relx=0.3, rely=0.49, relwidth=0.62, relheight=0.08)

    #bookInfo4 = StringVar()
   # bookInfo4.set("Available")

   # bookInfo4A = Radiobutton(root, text="Available", font=("Georgia 8"), variable=bookInfo4, value="Available", bg='Lavender', command=setAI)
    #bookInfo4A.pack( anchor = W )
    #bookInfo4A.place(relx=0.34,rely=0.615)

   # bookInfo4I = Radiobutton(root, text="Issued", font=("Georgia 8"), variable=bookInfo4, value="Issued", bg='Lavender', command=setAI)
    #bookInfo4.pack( anchor = W )
   # bookInfo4I.place(relx=0.475,rely=0.615)

        
    #Submit Button
    SubmitBtn = Button(root, text="Submit", font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5, command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root, text="Quit", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5, command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#addBook()

#use book;
#create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), publisher varchar(30), genre varchar(30), status varchar(30));
#create table books_issued(bid varchar(20) primary key, issueto varchar(30));