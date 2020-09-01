# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:08:28 2020

@author: aryav
"""
import sqlite3

def createuser():
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
        return "Some error happend!!!"
    
        
def login(data):
    createuser()
    try:
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
    print(data)
    return 1

def weblist(status):
    return ['facebook.com']

def delitem(data):
    print(data)
    return 1
def additem(data):
    print(data)
    return 1
def block(data):
    pass