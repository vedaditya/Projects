# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:40:10 2020

@author: vedaditya , Dhritiman Mukherjee 
"""


import random 
import sys
class TicTacToe:
    
    def __init__(self):
        print("Welcome to the game of Tic-Tac-toe")
        self.n=int(input("Enter the order of Tic-Tac-toe game:- "))
        if self.n<=0 or type(self.n)!=int:
            print("The order of matrrix is not in correct format ")
            self.__playAgain()
        print("Welcome to {0}*{0} the Tic-Tac-Toe game".format(self.n))
        self.name1=input('Enter your name:- ')
        self.name2=input("Enter your opponent name:- ")
        self.__basicInfo()
        
    def __basicInfo(self):
        n=random.choice((self.name1,self.name2))
        self.ke1='X'
        self.ke2='0'
        print(n,'''choose your symbol '0(zero)' or 'X' :-''',end='')
        k=str(input())
        if k!='X' and k!='0':
            print("Enter correct the correct symbol")
            self.__basicInfo()
        m=self.name2 if n==self.name1 else self.name1
        if k=='X':
            self.players={self.ke1:n,self.ke2:m}
        else:
            self.players={self.ke1:m,self.ke2:n}
        self.list1=[[ str(j+1)+str(i+1) for i in range(self.n)] for j in range(self.n)]
        print("The playboard is Ready, All the best!")
        self.__show()
        self.__conPlay()
        
    def __show(self):
        print("{0:-^{width}s}".format('',width=self.n*5))
        for i in range(self.n):
            for j in range(self.n):
                print(" {0:{width}s}|".format(self.list1[i][j],width=3),end='')
            print("\n{0:-^{width}s}".format('',width=self.n*5))
        
    
    def __playAgain(self):
        a=input('''Do you want to play again? Enter 'Y' for 'Yes' and 'N' for 'No' ''')
        if a=='Y':
            print("Welocome again")
            self.__basicInfo()
        else:
            print("Thank You")
            sys.exit()
                  
    def __EnterX(self):
         print("{} enter the position you want to write '{}' :- ".format(self.players[self.ke1],self.ke1))
         try:
             a=input("Value should be in same line as '11':- ")
             i,j=int(a[0]),int(a[1])
             if self.list1[i-1][j-1]==self.ke1 or self.list1[i-1][j-1]==self.ke2:
                 print("PLease Enter position that is vaccent:- ")
                 self.__EnterX()
             self.list1[i-1][j-1]=self.ke1
             self.__show()
         except:
            print("The format of input or value is invalid")
            self.__playAgain()
        
    def __Enter0(self):
         print("{} enter the position you want to write '{}' :- ".format(self.players[self.ke2],self.ke2))
         try:
             a=input("Value should be in same line as '11':- ")
             i,j=int(a[0]),int(a[1])
             if self.list1[i-1][j-1]==self.ke1 or self.list1[i-1][j-1]==self.ke2:
                 print("PLease Enter position that is vaccent:- ")
                 self.__Enter0()
             self.list1[i-1][j-1]=self.ke2
             self.__show()
         except:
            print("The format of input or value is invalid")
            self.__playAgain()
    
    def __conPlay(self):
        self.__EnterX()
        self.__checkWin()
        self.__Enter0()
        self.__checkWin()
        self.__conPlay()
    
    def __checkWin(self):
        self.__checkWinVer()
        self.__checkWinHor()
        self.__checkwinInner()
        self.__checkWinDraw()
        
    def __checkWinHor(self):
        for j in range(1,self.n-1):
            if self.list1[0][j-1]==self.list1[0][j]==self.list1[0][j+1]:
                print("Congratulations {}, You won the game".format(self.players[self.list1[0][j]]))
                self.__playAgain()
                break;
            elif self.list1[-1][j-1]==self.list1[-1][j]==self.list1[-1][j+1]:
                print("Congratulations {}, You won the game".format(self.players[self.list1[-1][j]]))
                self.__playAgain()
                break;
    def __checkWinVer(self):
        for i in range(1,self.n-1):
            if self.list1[i-1][0]==self.list1[i][0]==self.list1[i+1][0]:
                print("Congratulations {}, You won the game".format(self.players[self.list1[i][0]]))
                self.__playAgain()
                break;
            elif self.list1[i-1][-1]==self.list1[i][-1]==self.list1[i+1][-1]:
                print("Congratulations {}, You won the game".format(self.players[self.list1[i][-1]]))
                self.__playAgain()
                break;
        
        
    def __checkWinDraw(self):
        flag=0
        for i in range(self.n):
            for j in range(self.n):
                if len(self.list1[i][j])!=1:
                    flag=1
                    break;
            else:
                continue
            break;
        if flag==0:
            print("Congratulations to both of you! Both of you played well ")
            self.__playAgain()
            
                    
    def __checkwinInner(self):
        for i in range(1,self.n-1):
            for j in range(1,self.n-1):
                if self.list1[i-1][j-1]==self.list1[i][j]==self.list1[i+1][j+1] :       #diagonal1
                    print("Congratulations {}, You won the game".format(self.players[self.list1[i][j]]))
                    self.__playAgain()
                    break;
                elif self.list1[i-1][j+1]==self.list1[i][j]==self.list1[i+1][j-1]:    #diagonal2
                    print("Congratulations {}, You won the game".format(self.players[self.list1[i][j]]))
                    self.__playAgain()
                    break;
                    
                elif self.list1[i-1][j]==self.list1[i][j]==self.list1[i+1][j]:          #vertical
                    print("Congratulations {}, You won the game".format(self.players[self.list1[i][j]]))
                    self.__playAgain()
                    break;
                    
                elif self.list1[i][j-1]==self.list1[i][j]==self.list1[i][j+1] :          #horizontal
                    print("Congratulations {}, You won the game".format(self.players[self.list1[i][j]]))
                    self.__playAgain()
                    break;
            else:
                continue
            break;
                
          
TicTacToe()
