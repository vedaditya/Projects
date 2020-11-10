# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:20:54 2020

@author: Vedaditya
"""
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect='127.0.0.1'
def blocker(website_list):
    '''
    Parameters
    ----------
    website_list : TYPE :- List
        List of websites to be unblocked.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    try:
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website[0] in content:
                    pass
                else:
                    file.write(redirect+" "+website[0]+"\n")
        return 1
    except:
        return 'Some error happend!!'
    
def unblock(website_list ):
    '''
    

    Parameters
    ----------
    website_list : TYPE :- List
        List of websites to be unblocked.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    try:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website[0] in line for website in website_list):
                    file.write(line)
            file.truncate()
        return 1
    except:
        return "Some error happend!!"
def readWebInFile():
    '''
    

    Returns
    -------
    TYPE :- List
        list of website that are blocked at before or present in file

    '''
    try:
        website_list=[]
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if line[0]!='#' and len(line)>1:
                    website_list.append(line.split()[1])
        return website_list
    except:
        return 0