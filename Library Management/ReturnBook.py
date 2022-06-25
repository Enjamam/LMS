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
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table


allBid = [] #List To store all Book IDs

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()

    extractBid = "select bid from "+issueTable
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
                
            if check == 'Issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"
  
    print(bid in allBid)
    print(status)
    updateStatus = "update "+bookTable+" set status = 'Available' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allBid.clear()
    root.destroy()
    

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def returnBook(): 

    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
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
    Canvas1.config(bg="#C0C0C0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5, relief=GROOVE)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='#A9A9A9', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", font=("Georgia 10 bold"), bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.3)
        
    bookInfo1 = Entry(labelFrame,  font=("Georgia 10"), bd=4)
    bookInfo1.focus()
    bookInfo1.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root, text="Submit",font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5, command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root, text="Quit", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5, command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#returnBook()