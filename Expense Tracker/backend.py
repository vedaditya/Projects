# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:28:02 2020

@author: vedaditya
"""

import mysql.connector

class Backend:
    def __init__(self):
        self.__UID=None
        self.__connect()
        
    def __connect(self):                        #Connecting to database
        try:
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            db="expense"
            )
            self.cursor=self.mydb.cursor()
            return 1
        except :
            error="Error in connecting with Server, Please check connection"
            return error
            
    
    def verify(self,email,passwd):                                   #verifying the User Credentials
        connStatus=self.__connect()
        if connStatus==1:
            try:
                self.cursor.execute("SELECT User_id from users where email like '{}' and password like '{}' ".format(email.lower().strip(),passwd))    
                a=self.cursor.fetchone()
                if len(a)>0:
                    self.__UID=a[0]
                    return 1
                else:
                    raise Exception
            except:
                return "Either Email or Password is incorrect !!"
            finally:
                self.mydb.close()
        else:
            return connStatus
    
    def registration(self,name,email,passwd):               #Updating the database (users(email,passwd,name))  
        connStatus=self.__connect()
        if connStatus==1:    
            try:
                self.cursor.execute("INSERT users (User_id,Name,Email,Password) VALUES (NULL,'{}','{}','{}')".format
                                    (
                    name.title().strip(),
                    email.lower().strip(),
                    passwd)
                    )
                self.mydb.commit()
                return 1
            except:
                return "Email is already exist. Please Login to continue!!"
            finally:
                self.mydb.close()
        else:   
            return connStatus  
        
    def addAmount(self,datalist):
        try:
            if datalist[1]=="Expense":
                datalist[3]=-1*int(datalist[-1])
            else:
                datalist[2]="Income"
        except:
            return "Invalid Data, Please Enter carefully!!"
        connStatus=self.__connect()
        if connStatus==1:    
            try:
                self.cursor.execute("INSERT transaction (User_id,tr_id,Cat,Amount,Date,sysdate) VALUES ({},NULL,'{}',{},'{}',sysdate())".format
                                    (self.__UID,datalist[2],datalist[3],datalist[0]))
                self.mydb.commit()
                
                self.cursor.execute("update users set bal=bal+{} where User_id={}; ".format(datalist[3],self.__UID))
                self.mydb.commit()
                return 1
            except:
                return "Some Error Occured!!"
                
            finally:
                self.mydb.close()
        else:   
            return connStatus 
            
    
    def getbal(self):
        connStatus=self.__connect()
        if connStatus==1:
            try:
                self.cursor.execute("SELECT bal from users where User_id like '{}' ".format(self.__UID))    
                a=self.cursor.fetchone()
                if a is not None:
                    return a[0]
                else:
                    return 0
            finally:
                self.mydb.close()
        else:   
            return None
    
    def getName(self):
        connStatus=self.__connect()
        if connStatus==1:
            try:
                self.cursor.execute("SELECT Name from users where User_id like '{}' ".format(self.__UID))    
                a=self.cursor.fetchone()
                if a is not None:
                    return a[0]
                else:
                    return None
            finally:
                self.mydb.close()
        else:   
            return None
        
    def clearUID(self):                 #clearing the user Id
        self.__UID=None
        
    def Transactions(self):
        connStatus=self.__connect()
        if connStatus==1:
            try:
                self.cursor.execute("SELECT Date,Cat,Amount from transaction where User_id like '{}' order by Date desc,sysdate desc".format(self.__UID))    
                return self.cursor.fetchall()            
            finally:
                self.mydb.close()
        else:   
            return None
    
    def delTrans(self):
        connStatus=self.__connect()
        if connStatus==1:    
            try:
                self.cursor.execute("DELETE FROM transaction WHERE (User_id = {})".format(self.__UID))
                self.mydb.commit()
                
                self.cursor.execute("update users set bal={} where User_id={}; ".format(0,self.__UID))
                self.mydb.commit()
                return 1
            except:
                return "Some Error Occured!!"
                
            finally:
                self.mydb.close()
        else:   
            return connStatus 
    
    
    def createTable(self):                                  #function for craeting the Table inside 
        self.__connect()
        self.cursor.execute("""
        CREATE TABLE `Users` (
          `User_id` INT UNIQUE AUTO_INCREMENT,
          `Name` VARCHAR(100) NOT NULL,
          `Email` VARCHAR(100) NOT NULL UNIQUE,
          `Password` VARCHAR(100) NOT NULL,
          `Bal` FLOAT,
          PRIMARY KEY (`User_id`),
          KEY `Key` (`Name`, `Email`, `Password`, `Bal`)
        );
        
        ALTER TABLE `Users` ALTER `Bal` SET DEFAULT 0;
        
        CREATE TABLE `Transaction` (
          `User_id` INT  NOT NULL,
          `tr_id` INT UNIQUE NOT NULL AUTO_INCREMENT ,
          `Cat` VARCHAR(100),
          `Amount` FLOAT NOT NULL,
          `Date` VARCHAR(45),
          `sysdate` VARCHAR(45),
          PRIMARY KEY (`tr_id`),
          KEY `FK` (`User_id`),
          KEY `Key` (`Cat`, `Amount`, `Date`,`sysdate`)
        );  
        
        """ ) 
        self.mydb.close()
        
                