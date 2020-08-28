# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:27:00 2020

@author: vedaditya
"""

from tkinter import *
from backend import Backend
import requests
from tkinter import ttk
from functools import partial
from tkcalendar import DateEntry

b=Backend()
flag1=1

class Users:                                    #User calss for login and register new user
    def __init__(self):                          #initializing the GUI wih Login Page
        self.root=Tk()
        self.root.title("User Login")
        self.root.minsize(400,500)
        self.root.configure(background="#166353")


        self.loginPage()
        self.root.mainloop()

    def loginPage(self):                                                    #login Page starts
        self.clear()

        label1=Label(self.root,text="Login Page",bg='#166353',fg='#ffffff')            #First Label
        label1.configure(font=("Constantia",20,'bold'))
        label1.pack(pady=(40,20))


        self.email=Entry(self.root,borderwidth=3)                           #first Text Box for email
        self.email.configure(font=(0))
        self.email.pack(pady=(10,10))
        self.email.insert(END,"Email Id")
        self.email.bind("<FocusIn>",partial(self.default,self.email,"Email Id"))
        self.email.bind("<FocusOut>",partial(self.default,self.email,"Email Id"))

        self.passwd=Entry(self.root,borderwidth=3)                          #Second Text Box for Password
        self.passwd.configure(font=(0))
        self.passwd.pack(pady=(10,10))
        self.passwd.insert(0,"Password")
        self.passwd.bind("<FocusIn>",partial(self.default,self.passwd,"Password"))
        self.passwd.bind("<FocusOut>",partial(self.default,self.passwd,"Password"))

        login=Button(self.root,text="Login",width=28,height=1,command=self.login)   #login Button
        login.pack(pady=(10,10))

        reg=Button(self.root,text="New User? Register.",width=28,height=1,command=self.reg)   #registration Button
        reg.pack(pady=(10,10))

        close=Button(self.root,text="Close",width=28,height=1,command=self.closing)    #Close Button
        close.pack(pady=(10,10))

        self.result=Label(self.root,bg='#166353',fg='#ffffff')
        self.result.configure(font=("Constantia",10,'bold'))
        self.result.pack(pady=(20,8))

    def login(self):                                                        #checking the Email and password
        status=b.verify(self.email.get(),self.passwd.get())
        if status==1:
            message='Login Successfull!!'
            self.result.configure(text=message)
            self.root.after(1000,self.closing)
        else:
            message=status
            self.result.configure(text=message)
            self.root.after(1500,lambda:self.result.configure(text=" "))


    def closing(self):                                                               #closing The Program
        self.root.destroy()

    def clear(self):                                            #clearing the Window except the result label
        lis = self.root.pack_slaves()
        for l in lis:
            l.destroy()

    def registration(self):
        status=b.registration(self.Name.get(), self.email.get(), self.passwd.get())                           #register the user
        if  status==1:
            message="Registration Successfull!! Redirecting to Login Page"
            self.root.after(2000, self.loginPage)
        else:
            message=status
        self.result.configure(text=message)

    def loginAgain(self):                   #returning back to login page
        self.closing()
        global flag
        flag=1


    def reg(self):                                              #registration page
        self.clear()
        self.label1=Label(self.root,text="User Registration",bg='#166353',fg='#ffffff')      #upeer label
        self.label1.configure(font=("Constantia",20,'bold'))
        self.label1.pack(pady=(30,10))

        self.Name=Entry(self.root,borderwidth=3)                                #Name entry Box
        self.Name.configure(font=(0))
        self.Name.pack(pady=(10,10))
        self.Name.insert(0,"Your Name")
        self.Name.bind("<FocusIn>",partial(self.default,self.Name,"Your Name"))
        self.Name.bind("<FocusOut>",partial(self.default,self.Name,"Your Name"))


        self.email=Entry(self.root,borderwidth=3)                               #Email Id entry Box
        self.email.configure(font=(0))
        self.email.pack(pady=(10,10))
        self.email.insert(0,"Email Id")
        self.email.bind("<FocusIn>",partial(self.default,self.email,"Email Id"))
        self.email.bind("<FocusOut>",partial(self.default,self.email,"Email Id"))

        self.passwd=Entry(self.root,borderwidth=3)                              #Password Entry Box
        self.passwd.configure(font=(0))
        self.passwd.pack(pady=(10,10))
        self.passwd.insert(0,"Password")
        self.passwd.bind("<FocusIn>",partial(self.default,self.passwd,"Password"))
        self.passwd.bind("<FocusOut>",partial(self.default,self.passwd,"Password"))

        reg=Button(self.root,text="Confirm!",width=28,height=1,command=self.registration)             #Confirm button
        reg.pack(pady=(10,10))

        loga=Button(self.root,text="Return To Login Page",width=28,height=1,command=self.loginAgain)    #back to login page button
        loga.pack(pady=(10,10))

        close=Button(self.root,text="Close",width=28,height=1,command=self.closing)                  #close button
        close.pack(pady=(10,10))

        self.result=Label(self.root,bg='#166353',fg='#ffffff')
        self.result.configure(font=("Constantia",10,'bold'))
        self.result.pack(pady=(20,8))


    def default(self,tb,message,event):                     #resetting the default message on text Box
        current = tb.get()
        if current == message:
            tb.delete(0,END)
        elif current == "":
            tb.insert(0, message)

    def __del__(self):                                                          #Destrutor
        pass



class mainGUI(Users):                                   #GUI to record/show transactions

    def AddAmount(self):                                #adding Amount to db acc to type(income/Expense)
        date=self.EDate.get()
        typ=self.TYPE
        cat=self.CAT
        amount=self.Eamount.get()
        a=[date,typ,cat,amount]
        status=b.addAmount(a)
        if status==1:
            self.mess.configure(text="Added Successfully!!")
            self.getamount()
        else:
            self.mess.configure(text=status)
        self.GUI.after(1500,lambda:self.mess.configure(text=" "))

    def delTrans(self):                         #Deleting the transactions
        status=b.delTrans()
        if status ==1:
            self.mess.configure(text="Deleted Successfully!!")
            self.getamount()
            self.GUI.after(1500,lambda:self.mess.configure(text=" "))
        else:
            self.mess.configure(text=status)


    def getUserName(self):                                          #getting name of user
        self.name=b.getName()

    def __init__(self):                                                     #init method
        self.CAT=None
        self.TYPE="Expense"
        self.getUserName()
        self.expInc()

    def getamount(self):                                    #getting users current balance
        amount=b.getbal()
        self.totalbal.configure(text="Your Current Balance is  {} ".format(amount))


    def Transactions(self):                                     #getting all transactions of user
        datalist=b.Transactions()
        self.trn=Tk()
        self.trn.title('Expense ')
        self.trn.minsize(400,300)
        self.trn.configure(background="#166353")

        label1=Label(self.trn,text="Your Transactions",bg='#166353',fg='#ffffff')            #First Label
        label1.configure(font=("Constantia",20,'bold'))
        label1.grid(row=0,column=0,columnspan=2,padx=200, pady=(20,20))

        scrol=Scrollbar(self.trn)

        TVList=['Date(Year/Month/Date)','Category','Amount']
        TVExpense=ttk.Treeview(self.trn,column=TVList, show='headings',height=5)

        for i in TVList:
            TVExpense.heading(i, text=i.title())
        TVExpense.grid(row=1,column=0,padx=3,pady=3,ipady=50)

        scrol.grid(row=1,column=2,padx=10,pady=3,ipady=50)
        scrol.config(command=TVExpense.yview)
        TVExpense.configure(yscrollcommand=scrol.set)

        for data in datalist:
            TVExpense.insert('','end',values=data)

        cancel=Button(self.trn, text='Exit',command=lambda:self.trn.destroy() ,width=15)
        cancel.grid(row=2,column=0,padx=200,pady=20,sticky='w',ipadx=10,ipady=10,columnspan=2)

        self.trn.mainloop()


    def expInc(self):                                  #Income /expense main GUI
        self.GUI=Tk()
        self.GUI.title('Expense ')
        self.GUI.minsize(600,500)
        self.GUI.configure(background="#166353")

        label1=Label(self.GUI,text="Welcome {} !!".format(self.name),bg='#166353',fg='#ffffff')        #welcome messege
        label1.configure(font=("Constantia",20,'bold'))
        label1.grid(row=0,column=0,columnspan=3,padx=150, pady=(40,20))


        LDate=Label(self.GUI, text='Date',font=(None,18),bg="#166353",fg='#ffffff')             #Date label
        LDate.grid(row=1,column=0,padx=5,pady=5,sticky='w')

        self.EDate=DateEntry(self.GUI, width=19,date_pattern='yyyy-mm-dd', bg='red',fg='white',font=(None,18))            #Date Entry
        self.EDate.grid(row=1,column=1,padx=5,pady=5,sticky='w')



        LType=Label(self.GUI,text='Type',font=(None,18),bg="#166353",fg='#ffffff')              #Type lebel
        LType.grid(row=2,column=0,padx=5,pady=5,sticky='w')

        self.Dtype=StringVar()                                                      #Type choices
        choicestype={'Income','Expense'}
        self.Dtype.set('Expense')

        Type=OptionMenu(self.GUI,self.Dtype,*choicestype)
        Type.grid(row=2,column=1,padx=5,pady=5,ipadx=90,sticky='w')

        self.Dtype.trace('w', self.change_Type)


        Lcat=Label(self.GUI,text='Expense Category**',font=(None,18),bg="#166353",fg='#ffffff')       #Category label
        Lcat.grid(row=3,column=0,padx=5,pady=5,sticky='w')

        self.Dcat=StringVar()                                                                   #category Choices
        choiceCat={'Food','Clothing','Travel','Essentials','Personal','Medical','Others'}
        self.Dcat.set('Others')
        ECat=OptionMenu(self.GUI,self.Dcat,*choiceCat)
        ECat.grid(row=3,column=1,padx=5,pady=5,ipadx=90,sticky='w')

        self.Dcat.trace('w', self.change_Cat)



        Lamount=Label(self.GUI,text='Amount',font=(None,18),bg="#166353",fg='#ffffff')              #Amount lebel
        Lamount.grid(row=4,column=0,padx=5,pady=5,sticky='w')

        self.Eamount=Entry(self.GUI,font=(None,18))                                 #amount Entry Box
        self.Eamount.grid(row=4,column=1,padx=5,pady=5,sticky='w')



        Add=Button(self.GUI, text='Add',command=self.AddAmount ,width=15)               #add Button
        Add.grid(row=5,column=1,padx=5,pady=5,sticky='w',ipadx=10,ipady=10)


        income=Button(self.GUI, text='Show Transactions',command=self.Transactions, width=15)           #show transaction button
        income.grid(row=5,column=2,padx=5,pady=5,sticky='w',ipadx=10,ipady=10)


        cancel=Button(self.GUI, text='Exit',command=lambda:self.GUI.destroy() ,width=15)            #cancel Button
        cancel.grid(row=6,column=1,padx=5,pady=5,sticky='w',ipadx=10,ipady=10)


        bal0=Button(self.GUI, text='Delete all Transactions',command=self.delTrans, width=15)           #Deleting the transactions
        bal0.grid(row=6,column=2,padx=5,pady=5,sticky='w',ipadx=10,ipady=10)


        logout=Button(self.GUI, text='Logout',command=self.logout ,width=15)            #logout Button
        logout.grid(row=7,column=1,padx=5,pady=5,sticky='w',ipadx=10,ipady=10,columnspan=2)


        chnage=Button(self.GUI, text='Change Your Password',command=chpass ,width=15)            #Change password Button
        chnage.grid(row=7,column=2,padx=5,pady=5,sticky='w',ipadx=10,ipady=10,columnspan=2)

        self.totalbal=Label(self.GUI,bg='#166353',fg='#ffffff')                     #total Balance
        self.totalbal.configure(font=("Constantia",20,'bold'))
        self.totalbal.grid(row=8,column=0,padx=100,pady=5,columnspan=3)
        self.getamount()

        self.mess=Label(self.GUI,bg='#166353',fg='#ffffff')             #message label
        self.mess.configure(font=("Constantia",15,'bold'))
        self.mess.grid(row=9,column=0,padx=100,pady=5,columnspan=3)

        notice=Label(self.GUI,bg='#166353',fg='#ffffff',text="**Only Applicable For Expense")   #notice label
        notice.configure(font=("Constantia",10,'bold'))
        notice.grid(row=10,column=0,padx=5,pady=5,columnspan=2,sticky='w' )


        self.GUI.mainloop()

    def logout(self):                   #returning back to login page
        self.GUI.destroy()
        b.clearUID()
        global flag1
        flag1=1

    def change_Cat(self,*args):                         #Getting the changed value of drop down button Cat
        self.CAT=self.Dcat.get()

    def change_Type(self,*args):                        #Getting the changed value of drop down button Type
        self.TYPE=self.Dtype.get()

class chpass(Users):

    def __init__(self):
        self.root=Tk()
        self.root.title("Change Pssword")
        self.root.minsize(400,300)
        self.root.configure(background="#166353")


        label1=Label(self.root,text="Reset your password",bg='#166353',fg='#ffffff')            #First Label
        label1.configure(font=("Constantia",20,'bold'))
        label1.pack(pady=(40,20))

        self.Npasswd=Entry(self.root,borderwidth=3)                          #Text Box for Password
        self.Npasswd.configure(font=(0))
        self.Npasswd.pack(pady=(10,10))
        self.Npasswd.insert(0,"Password")
        self.Npasswd.bind("<FocusIn>",partial(self.default,self.Npasswd,"Password"))
        self.Npasswd.bind("<FocusOut>",partial(self.default,self.Npasswd,"Password"))


        reg=Button(self.root,text="Confirm!!",width=28,height=1,command=self.changePass)    #Confirm Button
        reg.pack(pady=(10,10))

        close=Button(self.root,text="Close",width=28,height=1,command=self.closing)
        close.pack(pady=(10,10))

        self.status=Label(self.root,bg='#166353',fg='#ffffff')
        self.status.configure(font=("Constantia",10,'bold'))
        self.status.pack(pady=(20,8))


        self.root.mainloop()

    def changePass(self):
        passwd=self.Npasswd.get()
        status=b.changePass(passwd)
        if status==1:
            self.status.configure(text="Password changed successfully")
            self.root.after(1000,self.closing)
        else:
            self.status.configure(text=status)

def execute():
    global flag
    while flag:
        flag=0
        Users()
    if b.getName() is not None:
        mainGUI()
while flag1:
    global flag
    flag=1
    flag1=0
    execute()
