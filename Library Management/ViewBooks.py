from tkinter import *
from tkinter import ttk
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
bookTable = "books" 
    

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)


def View(): 
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
        
    headingLabel = Label(headingFrame1, text="View Book", bg='black', fg='white', font=('Georgia',18, 'bold'), bd=5, relief=GROOVE)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='Lavender', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
###############
    tv = ttk.Treeview(labelFrame, columns=(1, 2, 3, 4, 5, 6), show='headings', height=11)
    tv.pack(side=LEFT)

    # column identifiers 
    tv["columns"] = ("1", "2", "3", "4", "5", "6")
  
    # Defining headings, other option is tree
    #tv['show'] = 'tree' 
    # width of columns and alignment 
    tv.column("1", width = 50, anchor ='w')
    tv.column("2", width = 100, anchor ='w')
    tv.column("3", width = 100, anchor ='w')
    tv.column("4", width = 95, anchor ='w')
    tv.column("5", width=60, anchor='w')
    tv.column("6", width=55, anchor='w')

    tv.heading(1, text="Book ID")
    tv.heading(2, text="Title")
    tv.heading(3, text="Author")
    tv.heading(4, text="Publisher")
    tv.heading(5, text="Genre")
    tv.heading(6, text="Quantity")

    sb = Scrollbar(labelFrame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)

    tv.config(yscrollcommand=sb.set)
    sb.config(command=tv.yview)
#################
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        idx = 0
        for i in cur:
            tv.insert(parent='', index=idx, iid=idx, values=(i[0],i[1],i[2],i[3],i[4],i[5]))
            idx+=1
    except:
        messagebox.showinfo("Error","Failed to fetch data from database")

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    
    quitBtn = Button(root, text="Quit", font=("Georgia 15 bold"), bg='#27282C', fg='#F41A05', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#View()