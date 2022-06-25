from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import sys
import os

# Add your own database name and password here to reflect in the code
myuser = "LMS"
mypass = "0000"
mydatabase= "account"

con = pymysql.connect(host="localhost",user=myuser,password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
librTable = "librarian"  # Librarian Table

def ViewLib():
    global chkData
    cur.execute('SELECT * FROM librarian WHERE UserName = %s', (LibrInfo.get()))
    # Fetch one record and return result
    chkData = cur.fetchone()
    if chkData:
        SubmitBtn = Button(root, text="Delete", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5, command=deleteLibrarian)
        SubmitBtn.place(relx=0.418,rely=0.813, relwidth=0.15,relheight=0.07)

        Label(root, text="%-45s%-25s%-10s"%('Full Name','UserName','Password'), font=("Georgia 8"), bg='Lavender',fg='#27282C').place(relx=0.22,rely=0.5)
        Label(root, text="--------------------------------------------------------------------------------------------", font=("Georgia 8"), bg='Lavender',fg='#27282C').place(relx=0.185,rely=0.53)
        getLib = "SELECT * FROM librarian WHERE UserName = %s"
        try:
            cur.execute(getLib, LibrInfo.get())
            con.commit()
            for i in cur:
                Label(root, text="%-30s%-25s%-10s"%(i[0],i[1],i[2]), font=("Georgia 8"), bg='Lavender',fg='#27282C').place(relx=0.22,rely=0.58)
        except:
            messagebox.showinfo("Error","Failed to fetch files from database")
    else:
        messagebox.showinfo("Finder", "Please check UserName")
        #delete()


def deleteLibrarian():
    UserName = LibrInfo.get()

    deletelibSql = "delete from " + librTable + " where UserName = '" + UserName + "'"
    if chkData:
        try:
            cur.execute(deletelibSql)
            con.commit()
            messagebox.showinfo('Success', "Librarian Record Deleted Successfully")
        except:
            messagebox.showinfo("Please check Librarian UserName")
    else:
        messagebox.showinfo('Failed',"Librarian is not Present, recheck")

    print(UserName)

    LibrInfo.delete(0, END)
    # root.destroy()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def deleteLibr():
    global LibrInfo, Canvas1, con, cur, librTable, root

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
    Canvas1.config(bg="#F5F5F5")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5, relief=GROOVE)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Librarian", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='Lavender', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    # Librarian UserName to Delete
    lb2 = Label(labelFrame, text="User Name : ", font=("Georgia 10 bold"), bg='#006B38', fg='white')
    lb2.place(relx=0.05, rely=0.1)

    LibrInfo = Entry(labelFrame, font=("Georgia 10"), bd=4)
    LibrInfo.focus()
    LibrInfo.place(relx=0.3, rely=0.1, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="Search",font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5, command=ViewLib)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5, command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

#deleteLibr()