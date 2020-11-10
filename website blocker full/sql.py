# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:08:28 2020

@author: vedaditya
"""
import sqlite3
from datetime import datetime as date
import fileedit as f
import time
def initial():
    '''
    
    Initialize and setting up the DBMS if not.
    Returns
    -------
    int
        

    '''
    try:
        if createuser()!=1:
            return 0
        website_list=f.readWebInFile()
        conn = sqlite3.connect('something.db')
        c=conn.cursor()
        for web in website_list:
            try:
                c.execute('''INSERT INTO websites VALUES (?)''',(web,))
            except:
                pass
        conn.commit()
        conn.close()
        return 1
    except:
        return 0

def createuser():
    '''
    
    Create a table in dbms if not present
    Returns
    -------
    int
        DESCRIPTION.

    '''
    try:
        conn = sqlite3.connect('something.db')
        c=conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (UserID NOT NULL PRIMARY KEY,Passwd)''')
        c.execute('''CREATE TABLE IF NOT EXISTS websites (sites NOT NULL PRIMARY KEY)''')
        try:
             c.execute('''INSERT INTO users VALUES ('admin','admin')''')
        except:
            pass;
        conn.commit()
        conn.close()
        return 1
    except:
         return 0
    
        
def login(data):
    '''
    

    Parameters
    ----------
    data : List
        [User ID, Password]

    Returns
    -------
    int
        Return 1 if userid and passwd is correct else 0

    '''
    
    try:
        if initial()!=1:
            return "Some Error Occured!!"
        conn = sqlite3.connect('something.db')
        c=conn.cursor()
        c.execute('SELECT * from users where UserID=? and Passwd=?',data)
        a=c.fetchone()
        if len(a)>0:
            return 1
        conn.close()
    except :
        return 'UserID or Password is incorrect!!' 
    
def changeID(data):
    '''
    

    Parameters
    ----------
    data : list
        [old user Id , Old Password , New userId , New Password ]

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    st=login([data[0],data[1]])
    if st==1:
        try:
            conn = sqlite3.connect('something.db')
            c=conn.cursor()
            c.execute('''DELETE from users where UserId=? ''',(str(data[0]),))
            c.execute('''INSERT INTO users VALUES (?)''',(str(data[2]),str(data[3])))
            conn.commit()
            conn.close()
            return 1
        except:
            return 'Some error happend! Please try with different UserId'
    else:
        return 'Old UserId or password is Incorrect!!'
            

def weblist():
    '''
    list of websites in table websites 

    Returns
    -------
    list or error
        list of websites

    '''
    try:
        conn = sqlite3.connect('something.db')
        c=conn.cursor()
        c.execute('SELECT * from websites')
        a=c.fetchall()
        conn.close()
        return a
    except:
        return "Sorry,Some Error Occured!!"

def delitem(data):
    '''
    

    Parameters
    ----------
    data : list
        [login status 1/0,delete website from table ]

    Returns
    -------
    1 or Error
        DESCRIPTION.

    '''
    if data[1] !=1:
        return 'Please login!!'
    try:
        conn = sqlite3.connect('something.db')
        c=conn.cursor()
        c.execute('''DELETE from websites where sites=? ''',(str(data[0]),))
        conn.commit()
        conn.close()
        return 1
    except:
        return "Sorry,Some Error Occured!!"
def additem(data):
    '''
    

    Parameters
    ----------
    data : list
        [login status 1/0,add website in table ]

    Returns
    -------
    1 or Error
        DESCRIPTION.

    '''
    if data[1] !=1:
        return 'Please login!!'
    try:
        conn = sqlite3.connect('something.db')
        c=conn.cursor()
        try:
            c.execute('''INSERT INTO websites VALUES (?)''',(str(data[0]),))
        except:
            return 'Duplicate website'
        conn.commit()
        conn.close()
        return 1
    except:
        return "Sorry,Some Error Occured!!"
    

def blockfn():
    '''
    function to call block website from fileedit.py

    Returns
    -------
    int
        DESCRIPTION.

    '''
    try:
        web=weblist()
        f.blocker(web)
    except:
        return 0
        
def unblockAll():
    '''
    

    Returns
    -------
    int
        Unblock all the 

    '''
    try:
        web=weblist()
        conn = sqlite3.connect('something.db')
        c=conn.cursor()
        c.execute('DROP TABLE websites')
        conn.commit()
        f.unblock(web)
        return 1
    except:
        return 0
  
        
def timediff(t1,t2):
    '''
    Parameters
    ----------
    t1 : STRING
        time in format HH:MM:SS
    t2 : STRING
        time in format HH:MM:SS

    Returns The difference btween t2 and t1(t2-t1)
    -------
    
    '''
    forma='%H:%M:%S'
    tdelta=time.gmtime((date.strptime(t2,forma)-date.strptime(t1,forma)).seconds)
    
    return time.strftime(forma,tdelta) 

def unblock(end):
    '''
    Parameters
    ----------
    end : STRING(HH:MM:SS)
        Time at fn will call unblockall function 

    Returns
    -------
    None.
    '''
    while True:
        currtime=date.now().strftime('%H:%M:%S')
        diff=timediff(currtime,end)
        if diff<='00:00:01':
            try:
                unblockAll()
            except:
                pass
            break;
        else:
            time.sleep(1)
            print(diff)
            

def block(start,end):
    '''
    Parameters
    ----------
    start : STRING(HH:MM:SS)
        start time to block 
    end : STRING(HH:MM:SS)
        time to unblock
    Returns
    -------
    None.
    '''
    
    currtime=date.now().strftime('%H:%M:%S')
    diff=timediff(currtime,start)
    if diff<='00:00:01':
        try:
            blockfn()
            unblock(end)
        except :
            pass

    else:
        while True:
            time.sleep(1)
            currtime=date.now().strftime('%H:%M:%S')
            diff=timediff(currtime,start)
            print(diff)
            if diff=='00:00:01':
                break
        block(start,end)
