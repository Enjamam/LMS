from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import sys
import os

# Add your own database name and password here to reflect in the code
myuser = "LMS"
mypass = "0000"
mydatabase = "student"

con = pymysql.connect(host="localhost", user=myuser, password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
studentTable = "students"  # Book Table


def setUp():
    global status
    status = studentInfo4.get()


def View():
    global chkData, studentInfo4, UpInfo1
    cur.execute('SELECT * FROM students WHERE ID = %s', (studentInfo1.get()))
    # Fetch one record and return result
    chkData = cur.fetchone()
    if chkData:
        Label(root, text="%-10s%-38s" % ('ID', 'Name'), font=("Georgia 8"),
              bg='Lavender', fg='black').place(relx=0.22, rely=0.47)
        Label(root,
              text="----------------------------------------------------------------------------------------------",
              font=("Georgia 8"), bg='Lavender', fg='black').place(relx=0.185, rely=0.5)
        getStudents = "SELECT * FROM students WHERE ID = %s"
        try:
            cur.execute(getStudents, studentInfo1.get())
            con.commit()
            for i in cur:
                Label(root, text="%-10s%-30s" % (i[0], i[1]), font=("Georgia 8"), bg='Lavender',
                      fg='black').place(relx=0.22, rely=0.53)

            SubmitBtn = Button(root, text="Update", font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5,
                               command=UpdateStudent)
            SubmitBtn.place(relx=0.418, rely=0.813, relwidth=0.15, relheight=0.07)

            # Book Status
            lb4 = Label(labelFrame, text="Update : ", font=("Georgia 8 bold"), bg='Lavender', fg='black')
            lb4.place(relx=0.17, rely=0.61, relheight=0.08)

            studentInfo4 = StringVar()
            studentInfo4.set("ID")

            Id = Radiobutton(root, text="ID", font=("Georgia 8"), variable=studentInfo4, relief=GROOVE, value="ID",
                              bg='Lavender', command=setUp)
            # bookInfo4A.pack( anchor = W )
            Id.place(relx=0.37, rely=0.60)

            NAme = Radiobutton(root, text="Name", font=("Georgia 8"), variable=studentInfo4, relief=GROOVE,
                                value="Name", bg='Lavender', command=setUp)
            # bookInfo4.pack( anchor = W )
            NAme.place(relx=0.50, rely=0.60)

            # Author = Radiobutton(root, text="Author", font=("Georgia 8"), variable=bookInfo4, relief=GROOVE,
            #                      value="author", bg='Lavender', command=setUp)
            # # bookInfo4.pack( anchor = W )
            # Author.place(relx=0.62, rely=0.60)

            # Book ID to Update
            lb2 = Label(labelFrame, text="Enter Data : ", font=("Georgia 10 bold"), bg='Lavender', fg='black',
                        relief=GROOVE)
            lb2.place(relx=0.05, rely=0.8)

            UpInfo1 = Entry(labelFrame, font=("Georgia 10"), bd=4)
            UpInfo1.focus()
            UpInfo1.place(relx=0.3, rely=0.8, relwidth=0.62)


        except:
            messagebox.showinfo("Error", "Failed to fetch files from database")
    else:
        messagebox.showinfo("Finder", "Please check Book ID")
        # Update()


def UpdateStudent():
    changeInfo = UpInfo1.get()
    ID = studentInfo1.get()

    UpdateSql = "UPDATE " + studentTable + " SET " + status + " = '" + changeInfo + "' WHERE ID = '" + ID + "'"
    if chkData:
        try:
            cur.execute(UpdateSql)
            con.commit()
            messagebox.showinfo('Success', "Book Record Updated Successfully")
            if status == "ID":
                studentInfo1.delete(0, END)
            UpInfo1.delete(0, END)
        except:
            messagebox.showinfo("Please check Book ID")
    else:
        studentInfo1.delete(0, END)
        UpInfo1.delete(0, END)
        # root.destroy()
        messagebox.showinfo('Failed', "Book is not Present, recheck")
    print(changeInfo)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def UpdateStu():
    global studentInfo1, Canvas1, con, cur, studentTable, root, labelFrame

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
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5, relief=GROOVE)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Update Student", bg='black', fg='white', font=('Georgia', 18, 'bold'), bd=5,
                         relief=GROOVE)
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='Lavender', bd=8, relief=GROOVE)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Update
    lb2 = Label(labelFrame, text="Student ID : ", font=("Georgia 10 bold"), bg='Lavender', fg='black', relief=GROOVE)
    lb2.place(relx=0.05, rely=0.1)

    studentInfo1 = Entry(labelFrame, font=("Georgia 10"), bd=4)
    studentInfo1.focus()
    studentInfo1.place(relx=0.3, rely=0.1, relwidth=0.62)

    # Submit Button
    SearchBtn = Button(root, text="Search", font=("Georgia 12 bold"), bg='#27282C', fg='#1BA644', bd=5, command=View)
    SearchBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font=("Georgia 12 bold"), bg='#27282C', fg='#F41A05', bd=5,
                     command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

#UpdateStu()