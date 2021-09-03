from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql


class connectorDB:
    def __init__(self, root):
        self.root = root
        titlespace = ""
        self.root.title(102 * titlespace + "Employee Management System")
        self.root.geometry("850x700+300+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, bd=10, width=770,
                          height=700, relief=RIDGE, bg='cadet blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770,
                           height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=7, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400,
                          padx=2, bg='cadet blue', relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600,
                           height=180, padx=2, pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP, padx=0, pady=0)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100,
                            height=400, padx=2, bg='cadet blue', relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90,
                             height=400, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)
        # ====================================================================================================================

        EmployID = StringVar()
        Name = StringVar()
        Age = StringVar()
        Post = StringVar()
        Salary = StringVar()
        # ======================================================================================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "MYSQL Connection", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.entEmployID.delete(0, END)
            self.entName.delete(0, END)
            self.entAge.delete(0, END)
            self.entPost.delete(0, END)
            self.entSalary.delete(0, END)

        def addData():
            if EmployID.get() == "" or Name.get() == "" or Age.get() == "":
                tkinter.messagebox.showerror(
                    "MYSQL connection", "enter correct Details")

            else:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", passwd="ckerryccc", database="trainee")
                cur = sqlCon.cursor()
                cur.execute("insert into trainee values(%s,%S,%s,%s,%s,%s,)", (

                EmployID.get(),
                Name.get(),
                Age.get(),
                Post.get(),
                Salary.get(),
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo(
                    "Data Entry Form", "Record Entered Successfully")

        def displayData():
            if EmployID.get() == "" or Name.get() == "" or Age.get() == "":
                tkinter.messagebox.showerror(
                    "MYSQL connection", "enter correct Details")

            else:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", passwd="ckerryccc", database="trainee")
                cur = sqlCon.cursor()
                cur.execute("select from employ")
                result = cur.fetchall()
                if len(result) != ():
                    self.employ_records.delete(
                        *self.employ_records.get_children())
                    for row in result:
                        self.employ_records.insert('', END, values=row)

                sqlCon.commit()
                displayData()
                sqlCon.close()
                tkinter.messagebox.showinfo(
                    "Data Entry Form", "Record Entered Successfully")

        def info(ev):
            viewInfo = self.employ_records.focus()
            learnerData = self.employ_records.item(viewInfo)
            row = learnerData['values']
            EmployID.set(row[0])
            Name.set(row[1])
            Age.set(row[2])
            Post.set(row[3])
            Salary.set(row[4])

        def update():
            sqlCon = pymysql.connect(
                host="localhost", user="root", passwd="ckerryccc", database="trainee")
            cur = sqlCon.cursor()
            cur.execute("update empoly set Name=%s,age=%S,post=%s,salary=%s,employid=%s,", (

                EmployID.get(),
                Name.get(),
                Age.get(),
                Post.get(),
                Salary.get(),
                ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Data Entry Form", "Record update Successfully")

        def Delete():
            sqlCon = pymysql.connect(
                host="localhost", user="root", passwd="ckerryccc", database="trainee")
            cur = sqlCon.cursor()
            cur.execute("delete from employ where emid=%s", EmployID.get())

            sqlCon.commit()
            displayData()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Data Entry Form", "Record Successfully delete")

        def search():
            try:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", passwd="ckerryccc", database="trainee")
                cur = sqlCon.cursor()
                cur.execute(
                    "select * from trainee where employid='%s'" % EmployID.get())

                row = cur.fetchone()

                EmployID.set(row[0])
                Name.set(row[1])
                Age.set(row[2])
                Post.set(row[3])
                Salary.set(row[4])
 
                sqlCon.commit()

            except:
            
                tkinter.messagebox.showinfo("Data Entry Form","No such record found")
                Reset()
                sqlCon.close()
        




        # ======================================================================================================================
        self.lbltitle=Label(TitleFrame,font=('arial',40,'bold'),text="Employee Management",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=132)

        self.lblEmployID=Label(LeftFrame1, font=('arial',12,'bold'),text="EmployID",bd=7)
        self.lblEmployID.grid(row=1,column=0,sticky=W,padx=5)
        self.entEmployID=Entry(LeftFrame1, font=('arial',12,'bold'),bd=7,width=44,justify='left',
        textvariable= EmployID)
        self.entEmployID.grid(row=1,column=1,sticky=W,padx=5)

        self.lblName=Label(LeftFrame1, font=('arial',12,'bold'),text="Name",bd=7)
        self.lblName.grid(row=2,column=0,sticky=W,padx=5)
        self.entName=Entry(LeftFrame1, font=('arial',12,'bold'),bd=7,width=44,justify='left',
        textvariable=Name)
        self.entName.grid(row=2,column=1,sticky=W,padx=5)

        self.lblAge=Label(LeftFrame1, font=('arial',12,'bold'),text="Age",bd=7)
        self.lblAge.grid(row=3,column=0,sticky=W,padx=5)
        self.entAge=Entry(LeftFrame1, font=('arial',12,'bold'),bd=7,width=44,justify='left',
        textvariable=Age)
        self.entAge.grid(row=3,column=1,sticky=W,padx=5)

        self.lblPost=Label(LeftFrame1, font=('arial',12,'bold'),text="Post",bd=7)
        self.lblPost.grid(row=4,column=0,sticky=W,padx=5)
        self.entPost=Entry(LeftFrame1, font=('arial',12,'bold'),bd=7,width=44,justify='left',
        textvariable=Post)
        self.entPost.grid(row=4,column=1,sticky=W,padx=5)

        self.lblSalary=Label(LeftFrame1, font=('arial',12,'bold'),text="Salary",bd=7)
        self.lblSalary.grid(row=5,column=0,sticky=W,padx=5)
        self.entSalary=Entry(LeftFrame1, font=('arial',12,'bold'),bd=7,width=44,justify='left',
        textvariable=Salary)
        self.entSalary.grid(row=5,column=1,sticky=W,padx=5)
        # ===========================================================================

        scroll_Y=Scrollbar(LeftFrame,orient=VERTICAL)
        self.employ_records=ttk.Treeview(LeftFrame,height=12,columns=("emid","Name","Age","Post","Salary"),yscrollcommand=scroll_Y.set)
        scroll_Y.pack(side=RIGHT,fill=Y)

        self.employ_records.heading("emid",text="Employ_id")
        self.employ_records.heading("Name",text="Name")
        self.employ_records.heading("Age",text="Age")
        self.employ_records.heading("Post",text="Post")
        self.employ_records.heading("Salary",text="Salary")

        self.employ_records['show']='headings'

        self.employ_records.column("emid",width=70)
        self.employ_records.column("Name",width=100)
        self.employ_records.column("Age",width=100)
        self.employ_records.column("Post",width=100)
        self.employ_records.column("Salary",width=70)

        self.employ_records.pack(fill =BOTH,expand=1)
        self.employ_records.bind("<ButtonRelease-1>",info)
        # ================================================

        self.btnAddNew=Button(RightFrame1a,font=('arial',16,'bold'),text="Add New",bd=4,pady=1,padx=24,
        width=8,height=2,command=addData).grid(row=0,column=0,padx=1)

        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold'),text="Diesplay",bd=4,pady=1,padx=24,
        width=8,height=2,command=displayData).grid(row=1,column=0,padx=1)

        self.btnUpdate=Button(RightFrame1a,font=('arial',16,'bold'),text="Update",bd=4,pady=1,padx=24,
        width=8,height=2,command=update).grid(row=2,column=0,padx=1)

        self.btnDelete=Button(RightFrame1a,font=('arial',16,'bold'),text="Delete",bd=4,pady=1,padx=24,
        width=8,height=2,command=Delete).grid(row=3,column=0,padx=1)

        self.btnSearch=Button(RightFrame1a,font=('arial',16,'bold'),text="Search",bd=4,pady=1,padx=24,
        width=8,height=2).grid(row=4,column=0,padx=1)

        self.btnReset=Button(RightFrame1a,font=('arial',16,'bold'),text="Reset",bd=4,pady=1,padx=24,
        width=8,height=2,command=Reset).grid(row=5,column=0,padx=1)

        self.btnExit=Button(RightFrame1a,font=('arial',16,'bold'),text="Exit",bd=4,pady=1,padx=24,
        width=8,height=2,command=iExit).grid(row=6,column=0,padx=1)
       # ============================================================================================



if __name__=='__main__':
    root =Tk()
    application=connectorDB(root)
    root.mainloop()
