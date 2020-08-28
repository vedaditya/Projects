# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:24:40 2020

@author: aryav
"""

from tkinter import *
from tkinter import ttk
from functools import partial

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
        status=1  #b.verify(self.email.get(),self.passwd.get())
        if status==1:
            message='Login Successfull!!'
            self.result.configure(text=message)
            self.closing()
            Main()
        else:
            message=status
            self.result.configure(text=message)

class chpass(adminlogin):
    
    def __init__(self):
        self.root=Tk()
        self.root.title("Change Pssword")
        self.root.minsize(400,300)
        self.root.configure(background="#166353")
        
        
        label1=Label(self.root,text="Change your password",bg='#166353',fg='#ffffff')            #First Label
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
        status=1 #b.changePass(passwd)
        if status==1:
            self.status.configure(text="Password changed successfully")
            self.root.after(1000,self.closing)
        else:
            self.status.configure(text=status)

class displayblock():
    def __init__(self):
        self.root=Tk()
        self.root.title("Working Hour")
        self.root.minsize(400,300)
        self.root.configure(background="#166353")
        
        
        label1=Label(self.root,text="Websites are blocked!!!",bg='#166353',fg='#ffffff')            #First Label
        label1.configure(font=("Constantia",20,'bold'))
        label1.pack(pady=(40,20))
        
        edit=Button(self.root,text="Edit the websites!!!",width=28,height=2,command=self.editsites)   #Unblock button
        edit.pack(pady=(10,20))
        
        close=Button(self.root,text="Unblock all websites!!!",width=28,height=2,command=self.unblockAll)   #Unblock button
        close.pack(pady=(10,20))
        
        self.status=Label(self.root,bg='#166353',fg='#ffffff')
        self.status.configure(font=("Constantia",10,'bold'))
        self.status.pack(pady=(20,8))
        
        self.root.mainloop()
        
    def unblockAll(self):
        pass
    
    def editsites(self):
        pass
    
    
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

        self.displays()   
            
        delete=Button(self.root, text='Delete selected',command=self.deleteitems ,width=15)               #delete Button
        delete.grid(row=2,column=1,padx=25,pady=5,sticky='w',ipadx=10,ipady=10)
        
        display=Button(self.root, text='Display',command=self.displays ,width=15)               #display Button
        display.grid(row=3,column=1,padx=25,pady=5,sticky='w',ipadx=10,ipady=10)
        
        starttime=Label(self.root, text='Start time',font=('Constantia' ,18),bg="#166353",fg='#ffffff')             #starttime label
        starttime.grid(row=4,column=0,padx=150,pady=5,sticky='w')
        
        self.sttime=Entry(self.root,borderwidth=3,width=13)                           #Text Box for dates
        self.sttime.configure(font=(0))
        self.sttime.grid(row=4,column=1,padx=25,pady=10,sticky='w')
        self.sttime.insert(END,"HH:MM:SS")
        self.sttime.bind("<FocusIn>",partial(self.default,self.sttime,"HH:MM:SS"))
        self.sttime.bind("<FocusOut>",partial(self.default,self.sttime,"HH:MM:SS"))
        
        endtime=Label(self.root, text='Stop Time',font=('Constantia',18),bg="#166353",fg='#ffffff')             #endtime label
        endtime.grid(row=5,column=0,padx=150,pady=5,sticky='w')
        
        self.entime=Entry(self.root,borderwidth=3,width=13)                           #Text Box for dates
        self.entime.configure(font=(0))
        self.entime.grid(row=5,column=1,padx=25,pady=10,sticky='w')
        self.entime.insert(END,"HH:MM:SS")
        self.entime.bind("<FocusIn>",partial(self.default,self.entime,"HH:MM:SS"))
        self.entime.bind("<FocusOut>",partial(self.default,self.entime,"HH:MM:SS"))
        
        startB=Button(self.root, text='Start',command=self.start ,width=63)               #start Button
        startB.grid(row=6,column=0,padx=100,pady=5,sticky='w',ipadx=10,ipady=10,columnspan=2)
        
        Chpassword=Button(self.root, text='Chnage Password',command=self.changepasswd ,width=20)               #change passwd Button
        Chpassword.grid(row=7,column=0,padx=75,pady=5,sticky='w',ipadx=10,ipady=10)
        
        logoutB=Button(self.root, text='Logout!',command=self.logout ,width=17)               #display Button
        logoutB.grid(row=7,column=1,padx=25,pady=5,sticky='w',ipadx=10,ipady=10)
        
        
        
    def displays(self):
        datalist=['facebook.com']
        for i in self.TVweb.get_children():
            self.TVweb.delete(i)
        
        for data in datalist:
            self.TVweb.insert('','end',values=data)
            
    def deleteitems(self):
        try:
            
            ite=self.TVweb.selection()[0]
            print(self.TVweb.item(ite)['values'])
            self.TVweb.delete(ite)
            
        except:
            pass
        
    def Addwebsite(self):
        data=self.site.get()
        self.TVweb.insert('','end',values=data)
        
    def checktime(self):
        pass
    
    def start(self):
        self.closing()
        displayblock()
        
    def changepasswd(self):
        chpass()
    def logout(self):
        self.closing()
        global status
        status=0
        adminlogin()
        
        
adminlogin()
