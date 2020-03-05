

#INSTRUCTIONS 

Read these instructions before before executing these python script.

This project is on expense tracker, On which you can add you incomes and expenses with the category of expenses made by you on regular basis and view your all transactions that you have made in that month after login into your account by your email id and password.If you are a new user you can register your details through registration Page.


Requirements:-
1. Make sure your Laptop/Desktop should have the python environment.
2. Make sure the below given modules are installed in your python environment:
	a. tkinter 
	b. requests
	c. **mysql (Mysql Python connector)
	d. **tkcalender 
	e. functools
**3. Make sure you have installed the sql server and created the database with name the name "expense" and set the password of databse to '1234'.
**4. first time for creating the tables inside the database expense run the createTable() function inside the Backend class in backend.py or execute the following commands on your python terminal.
		a. from backend import Backend
		b. b=Backend
		c. c.createTable()
	

  Some of them are by default comes with python but you will need to install some of these by using pip installer (If you don't have pip in you PC, Install it. For more information/help reffer to he links).

  The process to install any module by pip/pip3 are given below:
  	1. Run the cmd as administrator for IDLE/Python or respective terminal for other editor(like anaconda terminal for spyder/Jupyter/conda based editor)
	2. Run the command 'pip install mysql' (for installing mysql)
	3. You will get a success message after successflly installing the module.


 You can also check the availblity of library by importing the module using 'import moduleName' keyword.

Given below the links for taking extra help for installing the module in the python environment:
	https://docs.python.org/3/installing/index.html
	https://packaging.python.org/tutorials/installing-packages/
	https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation (For installing Python and pip in your PC)

