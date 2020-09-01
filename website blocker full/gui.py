# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:24:40 2020

@author: Vedaditya
"""

from tkinter import *
from tkinter import ttk
from functools import partial
import sql as s

global status


class adminlogin():

    def __init__(self):
        global status
        status=0
        self.root=Tk()
        self.root.title("Admin Login")
        self.root.minsize(400,400)
        self.root.configure(background="#166353")

        self.loginPage()
        self.root.mainloop()


    def loginPage(self):                                                    #login Page starts

        label1=Label(self.root,text="Login Page",bg='#166353',fg='#ffffff')            #First Label
        label1.configure(font=("Constantia",20,'bold'))
        label1.pack(pady=(40,20))


        self.email=Entry(self.root,borderwidth=3)                           #first Text Box for email
        self.email.configure(font=(0))
        self.email.pack(pady=(10,10))
        self.email.insert(END,"User Id")
        self.email.bind("<FocusIn>",partial(self.default,self.email,"User Id"))
        self.email.bind("<FocusOut>",partial(self.default,self.email,"User Id"))

        self.passwd=Entry(self.root,borderwidth=3)                          #Second Text Box for Password
        self.passwd.configure(font=(0))
        self.passwd.pack(pady=(10,10))
        self.passwd.insert(0,"Password")
        self.passwd.bind("<FocusIn>",partial(self.default,self.passwd,"Password"))
        self.passwd.bind("<FocusOut>",partial(self.default,self.passwd,"Password"))

        login=Button(self.root,text="Login",width=28,height=1,command=self.login)   #login Button
        login.pack(pady=(10,10))


        close=Button(self.root,text="Close",width=28,height=1,command=self.closing)    #Close Button
        close.pack(pady=(10,10))

        self.result=Label(self.root,bg='#166353',fg='#ffffff')
        self.result.configure(font=("Constantia",10,'bold'))
        self.result.pack(pady=(20,8))


    def closing(self):                                                               #closing The Program
        self.root.destroy()


    def default(self,tb,message,event):                     #resetting the default message on text Box
        current = tb.get()
        if current == message:
            tb.delete(0,END)
        elif current == "":
            tb.insert(0, message)

    def login(self):                                                      #checking the Email and password
        global status
        stat=s.login([self.email.get(),self.passwd.get()])
        if stat==1:
            status=1
            message='Login Successfull!!'
            self.result.configure(text=message)
            self.closing()
            Main()
        else:
            message=stat
            self.result.configure(text=message)
            self.root.after(1500,lambda:self.result.configure(text=" "))

class chpass(adminlogin):

    def __init__(self):
        self.root=Tk()
        self.root.title("Change Pssword")
        self.root.minsize(400,300)
        self.root.configure(background="#166353")


        label1=Label(self.root,text="Change your UserId and Password",bg='#166353',fg='#ffffff')            #First Label
        label1.configure(font=("Constantia",20,'bold'))
        label1.pack(pady=(40,20))

        self.Nid=Entry(self.root,borderwidth=3)                          #Text Box for Password
        self.Nid.configure(font=(0))
        self.Nid.pack(pady=(10,10))
        self.Nid.insert(0,"New User ID")
        self.Nid.bind("<FocusIn>",partial(self.default,self.Nid,"New User ID"))
        self.Nid.bind("<FocusOut>",partial(self.default,self.Nid,"New User ID"))

        self.Npasswd=Entry(self.root,borderwidth=3)                          #Text Box for Password
        self.Npasswd.configure(font=(0))
        self.Npasswd.pack(pady=(10,10))
        self.Npasswd.insert(0,"Password")
        self.Npasswd.bind("<FocusIn>",partial(self.default,self.Npasswd,"Password"))
        self.Npasswd.bind("<FocusOut>",partial(self.default,self.Npasswd,"Password"))


        reg=Button(self.root,text="Confirm!!",width=28,height=1,command=self.changePassUser)    #Confirm Button
        reg.pack(pady=(10,10))

        close=Button(self.root,text="Close",width=28,height=1,command=self.closing)
        close.pack(pady=(10,10))

        self.statuss=Label(self.root,bg='#166353',fg='#ffffff')
        self.statuss.configure(font=("Constantia",10,'bold'))
        self.statuss.pack(pady=(20,8))

        self.root.mainloop()

    def changePassUser(self):
        global status
        data=[self.Nid.get(),self.Npasswd.get(),status]
        stat=s.changeID(data)
        if stat==1:
            self.statuss.configure(text="Changed successfully!!!")
            self.root.after(1000,self.closing)
        else:
            self.statuss.configure(text=stat)

class displayblock():
    def __init__(self,start,end):

        self.start=start
        self.end=end
        self.GUI()


    def GUI(self):
        self.root=Tk()
        self.root.title("Blocker")
        self.root.minsize(400,300)
        self.root.configure(background="#166353")

        label1=Label(self.root,text="Welcome!!!",bg='#166353',fg='#ffffff')            #First Label
        label1.configure(font=("Constantia",20,'bold'))
        label1.pack(pady=(40,20))

        edit=Button(self.root,text="Edit the websites!!!",width=28,height=2,command=self.editsites)   #Edit button
        edit.pack(pady=(10,20))

        close=Button(self.root,text="Unblock all websites!!!",width=28,height=2,command=self.unblockAll)   #Unblock button
        close.pack(pady=(10,20))

        self.sta=Label(self.root,bg='#166353',fg='#ffffff')                  #messege label
        self.sta.configure(font=("Constantia",20,'bold'))
        self.sta.pack(pady=(20,8))

        self.block()

        self.root.mainloop()



    def unblockAll(self):
        pass

    def editsites(self):
        pass

    def block(self):
        self.sta.configure(text="Blocked!!!")


class Main(adminlogin):
    def __init__(self):
        self.root=Tk()
        self.root.title("Website Blocker")
        self.root.minsize(600,600)
        self.root.configure(background="#166353")
        self.TheGUI()
        self.root.mainloop()

    def TheGUI(self):
        label1=Label(self.root,text="Welocome to website blocker",bg='#166353',fg='#ffffff')            #First Label
        label1.configure(font=("Constantia",20,'bold'))
        label1.grid(row=0,column=0,columnspan=3,padx=150, pady=(40,20))


        self.site=Entry(self.root,borderwidth=3)                           #Text Box for sites
        self.site.configure(font=(0))
        self.site.grid(row=1,column=0,padx=50,pady=10,sticky='w',ipadx=38)
        self.site.insert(END,"Website")
        self.site.bind("<FocusIn>",partial(self.default,self.site,"Website"))
        self.site.bind("<FocusOut>",partial(self.default,self.site,"Website"))

        Add=Button(self.root, text='Add',command=self.Addwebsite ,width=15)               #add Button
        Add.grid(row=1,column=1,padx=25,pady=5,sticky='w',ipadx=10,ipady=10)


        TVList=['Websites']
        self.TVweb=ttk.Treeview(self.root,column=TVList, show='headings',height=5)

        for i in TVList:
            self.TVweb.heading(i, text=i.title())
        self.TVweb.grid(row=2,column=0,padx=50,pady=5,ipadx=50,sticky='w',rowspan=2)



        delete=Button(self.root, text='Delete selected',command=self.deleteitems ,width=15)               #delete Button
        delete.grid(row=2,column=1,padx=25,pady=5,sticky='w',ipadx=10,ipady=10)

        display=Button(self.root, text='Display',command=self.displays ,width=15)               #display Button
        display.grid(row=3,column=1,padx=25,pady=5,sticky='w',ipadx=10,ipady=10)

        starttime=Label(self.root, text='Start time(In 24 hour format):',font=('Constantia' ,18),bg="#166353",fg='#ffffff')             #starttime label
        starttime.grid(row=4,column=0,padx=75,pady=5,sticky='w')

        self.sttime=Entry(self.root,borderwidth=3,width=13)                           #Text Box for dates
        self.sttime.configure(font=(0))
        self.sttime.grid(row=4,column=1,padx=25,pady=10,sticky='w')
        self.sttime.insert(END,"00:00:00")
        self.sttime.bind("<FocusIn>",partial(self.default,self.sttime,"00:00:00"))
        self.sttime.bind("<FocusOut>",partial(self.default,self.sttime,"00:00:00"))

        endtime=Label(self.root, text='Stop Time(In 24 hour format):',font=('Constantia',18),bg="#166353",fg='#ffffff')             #endtime label
        endtime.grid(row=5,column=0,padx=75,pady=5,sticky='w')

        self.entime=Entry(self.root,borderwidth=3,width=13)                           #Text Box for dates
        self.entime.configure(font=(0))
        self.entime.grid(row=5,column=1,padx=25,pady=10,sticky='w')
        self.entime.insert(END,"00:00:00")
        self.entime.bind("<FocusIn>",partial(self.default,self.entime,"00:00:00"))
        self.entime.bind("<FocusOut>",partial(self.default,self.entime,"00:00:00"))

        startB=Button(self.root, text='Start',command=self.start ,width=20)               #start Button
        startB.grid(row=6,column=0,padx=75,pady=5,sticky='w',ipadx=10,ipady=10)

        Chpassword=Button(self.root, text='Chnage UserID & Password',command=self.changepasswd ,width=20)               #change passwd Button
        Chpassword.grid(row=7,column=0,padx=75,pady=5,sticky='w',ipadx=10,ipady=10)

        logoutB=Button(self.root, text='Logout!',command=self.logout ,width=17)               #display Button
        logoutB.grid(row=7,column=1,padx=25,pady=5,sticky='w',ipadx=10,ipady=10)

        self.mess=Label(self.root,bg='#166353',fg='#ffffff')             #message label
        self.mess.configure(font=("Constantia",15,'bold'))
        self.mess.grid(row=8,column=0,padx=100,pady=5,columnspan=3)

        self.displays()


    def displays(self):
        try:
            global status
            datalist=s.weblist(status)
            for i in self.TVweb.get_children():
                self.TVweb.delete(i)

            for data in datalist:
                self.TVweb.insert('','end',values=data)
            self.mess.configure(text='List Updated!!')
            self.root.after(1500,lambda:self.mess.configure(text=" "))
        except:
            self.mess.configure(text='Sorry,Some Error Occured!! ')
            self.root.after(1500,lambda:self.mess.configure(text=" "))

    def deleteitems(self):
        try:
            global status
            ite=self.TVweb.selection()[0]
            value=self.TVweb.item(ite)['values']
            if s.delitem([value,status])==1:
                self.TVweb.delete(ite)
                self.mess.configure(text='List Updated!!')
                self.root.after(1500,lambda:self.mess.configure(text=" "))
            else:
                raise Exception

        except:
            self.mess.configure(text='Sorry,Some Error Occured!! ')
            self.root.after(1500,lambda:self.mess.configure(text=" "))

    def Addwebsite(self):
        global status
        try:
            data=self.site.get()
            if s.additem([data,status])==1:
                self.TVweb.insert('','end',values=data)
                self.mess.configure(text='List Updated!!')
                self.root.after(1500,lambda:self.mess.configure(text=" "))
            else:
                raise Exception
        except:
            self.mess.configure(text='Sorry,Some Error Occured!! ')
            self.root.after(1500,lambda:self.mess.configure(text=" "))

    def checktime(self,time):
        try:
            a,b,c=map(int,time.split(":"))
            if a<0 or a>23:
                return False
            if b<0 or b>59:
                return False
            if c<0 or c>59:
                return False
            else:
                return True
        except:
            return False


    def start(self):
        start=self.sttime.get()
        end=self.entime.get()
        try:
            if self.checktime(start) and self.checktime(end):
                self.closing()
                displayblock(start,end)
            else:
                self.mess.configure(text='Please Enter valid time')
                self.root.after(1500,lambda:self.mess.configure(text=" "))
        except:
            self.mess.configure(text='Sorry,Some Error Occured!!')
            self.root.after(1500,lambda:self.mess.configure(text=" "))
    def changepasswd(self):
        try:
            chpass()
        except:
            self.mess.configure(text='Sorry,Some Error Occured!! ')
            self.root.after(1500,lambda:self.mess.configure(text=" "))

    def logout(self):
        try:
            self.closing()
            global status
            status=0
            adminlogin()
        except:
            self.mess.configure(text='Sorry,Some Error Occured!! ')
            self.root.after(1500,lambda:self.result.configure(text=" "))


adminlogin()
