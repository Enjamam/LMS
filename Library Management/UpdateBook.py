from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import sys
import os

# Add your own database name and password here to reflect in the code
myuser = "LMS"
mypass = "0000"
mydatabase= "book"

con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table

def setUp():
    global status
    status = bookInfo4.get()

def View():
    global chkData, bookInfo4, UpInfo1
    cur.execute('SELECT * FROM books WHERE bid = %s', (bookInfo1.get()))
    # Fetch one record and return result
    chkData = cur.fetchone()
    if chkData:
        Label(root, text="%-10s%-38s%-38s%-20s"%('BID','Title','Author','Publisher'), font=("Georgia 8"), bg='Lavender',fg='black').place(relx=0.22,rely=0.47)
        Label(root, text="----------------------------------------------------------------------------------------------", font=("Georgia 8"), bg='Lavender',fg='black').place(relx=0.185,rely=0.5)
        getBooks = "SELECT * FROM books WHERE bid = %s"
        try:
            cur.execute(getBooks, bookInfo1.get())
            con.commit()
            for i in cur:
                Label(root, text="%-10s%-30s%-32s%-20s"%(i[0],i[1],i[2],i[3]), font=("Georgia 8"), bg='Lavender',fg='black').place(relx=0.22,rely=0.53)
            
            SubmitBtn = Button(root, text="Update", font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5, command=UpdateBook)
            SubmitBtn.place(relx=0.418,rely=0.813, relwidth=0.15,relheight=0.07)

            # Book Status
            lb4 = Label(labelFrame,text="Update : ", font=("Georgia 8 bold"), bg='Lavender', fg='black')
            lb4.place(relx=0.17,rely=0.61, relheight=0.08)

            bookInfo4 = StringVar()
            bookInfo4.set("bid")

            BId = Radiobutton(root, text="Book ID", font=("Georgia 8"), variable=bookInfo4, relief=GROOVE, value="bid", bg='Lavender', command=setUp)
            #bookInfo4A.pack( anchor = W )
            BId.place(relx=0.37,rely=0.60)

            Title = Radiobutton(root, text="Title", font=("Georgia 8"), variable=bookInfo4, relief=GROOVE, value="title", bg='Lavender', command=setUp)
            #bookInfo4.pack( anchor = W )
            Title.place(relx=0.50,rely=0.60)

            Author = Radiobutton(root, text="Author", font=("Georgia 8"), variable=bookInfo4, relief=GROOVE, value="author", bg='Lavender', command=setUp)
            #bookInfo4.pack( anchor = W )
            Author.place(relx=0.62,rely=0.60)

            # Book ID to Update
            lb2 = Label(labelFrame,text="Enter Data : ", font=("Georgia 10 bold"), bg='Lavender', fg='black', relief=GROOVE)
            lb2.place(relx=0.05,rely=0.8)
        
            UpInfo1 = Entry(labelFrame, font=("Georgia 10"), bd=4)
            UpInfo1.focus()
            UpInfo1.place(relx=0.3,rely=0.8, relwidth=0.62)


        except:
            messagebox.showinfo("Error", "Failed to fetch files from database")
    else:
        messagebox.showinfo("Finder", "Please check Book ID")
        #Update()

def UpdateBook():
    changeInfo = UpInfo1.get()
    bid = bookInfo1.get()
    
    UpdateSql = "UPDATE "+bookTable+" SET "+status+" = '"+changeInfo+"' WHERE bid = '"+bid+"'"
    if chkData:
        try:
            cur.execute(UpdateSql)
            con.commit()
            messagebox.showinfo('Success',"Book Record Updated Successfully")
            if status == "bid":
                bookInfo1.delete(0, END)
            UpInfo1.delete(0, END)
        except:
            messagebox.showinfo("Please check Book ID")
    else:
        bookInfo1.delete(0, END)
        UpInfo1.delete(0, END)
    #root.destroy()
        messagebox.showinfo('Failed',"Book is not Present, recheck")
    print(changeInfo)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)

    
def Update(): 
    global bookInfo1, Canvas1, con,cur, bookTable, root, labelFrame
    
    root = Tk()
    root.title("IIUC Central Library")
    pathLogo = resource_path("logo.ico")
    root.iconbitmap(pathLogo)
    #img = PhotoImage('logo.png')
    #root.iconphoto(True, img)
    root.resizable(0,0)
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg='#F5F5F5')
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5, relief=GROOVE)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Update Book", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='Lavender', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Update
    lb2 = Label(labelFrame,text="Book ID : ", font=("Georgia 10 bold"), bg='Lavender', fg='black', relief=GROOVE)
    lb2.place(relx=0.05,rely=0.1)
        
    bookInfo1 = Entry(labelFrame, font=("Georgia 10"), bd=4)
    bookInfo1.focus()
    bookInfo1.place(relx=0.3,rely=0.1, relwidth=0.62)
    
    #Submit Button
    SearchBtn = Button(root, text="Search",font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5, command=View)
    SearchBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root, text="Quit", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5, command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#Update()