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
issueTable = "books_issued" 
bookTable = "books" #Book Table

def View():
    global chkData
    cur.execute('SELECT * FROM books WHERE bid = %s', (bookInfo1.get()))
    # Fetch one record and return result
    chkData = cur.fetchone()
    if chkData:
        SubmitBtn = Button(root, text="Delete", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5, command=deleteBook)
        SubmitBtn.place(relx=0.418,rely=0.813, relwidth=0.15,relheight=0.07)

        Label(root, text="%-10s%-38s%-38s%-20s"%('BID','Title','Author','Publisher'), font=("Georgia 8"), bg='Lavender',fg='black').place(relx=0.22,rely=0.5)
        Label(root, text="----------------------------------------------------------------------------------------------", font=("Georgia 8"), bg='Lavender',fg='black').place(relx=0.185,rely=0.53)
        getBooks = "SELECT * FROM books WHERE bid = %s"
        try:
            cur.execute(getBooks, bookInfo1.get())
            con.commit()
            for i in cur:
                Label(root, text="%-10s%-20s%-32s%-10s"%(i[0],i[1],i[2],i[3]), font=("Georgia 8"), bg='Lavender',fg='black').place(relx=0.22,rely=0.58)
        except:
            messagebox.showinfo("Failed to fetch files from database")
    else:
        messagebox.showinfo("Finder", "Please check Book ID")
        #delete()


def deleteBook():
    bid = bookInfo1.get()
    
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    if chkData:
        try:
            cur.execute(deleteSql)
            con.commit()
            cur.execute(deleteIssue)
            con.commit()
            messagebox.showinfo('Success',"Book Record Deleted Successfully")
        except:
            messagebox.showinfo("Please check Book ID")
    else:
        messagebox.showinfo('Failed',"Book is not Present, recheck")
    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
    

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def delete(): 
    global bookInfo1, Canvas1, con,cur, bookTable, root
    
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
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='Lavender', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", font=("Georgia 10 bold"), bg='Lavender', fg='black')
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

#delete()