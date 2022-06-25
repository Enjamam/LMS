from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import sys
import os
from ttkwidgets.autocomplete import AutocompleteEntryListbox

# Add your own database name and password here to reflect in the code
myuser = "LMS"
mypass = "0000"
mydatabase= "book"

con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books"
    
#List To store all Book IDs
allBid = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    bid = inf1.get()
    issueto = inf2.get()

    #issueBtn.destroy()
    #labelFrame.destroy()
    #lb1.destroy()
    #inf1.destroy()
    #inf2.destroy()
    
    
    extractBid = "select bid from "+bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'Available':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'Issued' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            #root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    
    allBid.clear()

def getliS():
    global IDstu
    # Add your own database name and password here to reflect in the code
    myuser = "LMS"
    mypass = "0000"
    mydatabase= "student"

    con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    studentTable = "students"
    IDstu=[]

    getStu = "select * from "+studentTable
    try:
        cur.execute(getStu)
        con.commit()
        for i in cur:
            IDstu.append(i[0])
    except:
        messagebox.showinfo("Failed to fetch files from database")

def getli():
    global bids
    # Add your own database name and password here to reflect in the code
    myuser = "LMS"
    mypass = "0000"
    mydatabase= "book"

    con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"
    bids=[]

    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            bids.append(i[0])
    except:
        messagebox.showinfo("Failed to fetch files from database")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    getli()
    getliS()
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
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='Lavender', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", font=("Georgia 8 bold"), bg='#F5F5F5', fg='black')
    lb1.place(relx=0.07,rely=0.1)
   
    #inf1 = Entry(labelFrame)
    inf1 = AutocompleteEntryListbox(labelFrame, completevalues=bids)
    inf1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.35)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", font=("Georgia 8 bold"), bg='#F5F5F5', fg='black')
    lb2.place(relx=0.07,rely=0.5)
        
    #inf2 = Entry(labelFrame)
    inf2 = AutocompleteEntryListbox(labelFrame, completevalues=IDstu)
    inf2.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.35)
    
    
    #Issue Button
    issueBtn = Button(root, text="Issue",font=("Georgia 15 bold"), bg='#27282C', fg='#1BA644', bd=5, command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root, text="Quit", font=("Georgia 15 bold"), bg='#27282C', fg='#F41A05', bd=5, command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

#issueBook()