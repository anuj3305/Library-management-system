-------------------------------- README FILE ------------------------------------
This project is created and tested on a Windows machine. 

Frameworks used :
1. Django 1.11.6 

Languages used :
1. Python 2.7
2. MYSQL 5.7
3. HTML
4. CSS
5. JavaScript
6. Ajax
7. AngularJS

Frameworks used :
1. Django 1.11.6 


Libraries/packages used: 
1. mysql-connector.c (6.1)
2. MySQL-python (1.2.5)
3. python-dateutil (2.6.0)
4. pytz (2016.10)
5. pip (9.0.1)
6. pyparsing (2.1.10)
7. bootstrap-toolkit


Instructions to execute: (Windows)
1. Open cmd terminal on windows (admin mode).
2. cd to the project directory
3. run 'python sqlgenerator.py'. This will generate library.sql file in the same location itself.
4. type in mysql -u root -p and enter the root password. Now you can see that the mysql has started
5. create a library database using the following commands:
   i. CREATE DATABASE LIBRARY DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
   ii. USE LIBRARY;
   iii. 'source' followed by project directory's path. This will dump the library.sql file into our database.
6. Modify 'sqlgenerator.py' by editing the path of 'books.csv' and 'borrowers.csv' files.
7. Modify 'settings.py': 
   i. Edit the root password.
   ii. Change 'templates' path mentioned under 'TEMPLATES_DIRS'. Also change 'STATICFILES_DIRS'. 
6. In a new cmd terminal (admin mode), type 'cd' followed by the project's directory [where 'manage.py' exists]. Hit Enter.
7. Run the following commands:
	i. "python manage.py makemigrations polls"
	ii. "python manage.py migrate"
	iii. "python manage.py runserver" 
8. Open your web browser and type http://127.0.0.1:8000/ to access the UI