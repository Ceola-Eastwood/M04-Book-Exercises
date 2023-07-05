
#16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. 
#As in 16.6, select and print the title column from the book table in alphabetical order.

#*****I am having issues with the SQLalchemy/engine.  
#Seems there was some kind of support update for it jan 2023 and i need to move on to other things.
#https://github.com/dagster-io/dagster/discussions/11881 

>>> import sqlalchemy
>>> conn = sqlalchemy.create_engine('sqlite:///books.db')
>>> sql = 'select title from book order by title asc'
>>> rows = conn.execute(sql)
>>> for row in rows:
...     print(row)
...
('Perdido Street Station',)
('Small Gods',)
('The Spellman Files',)
('The Weirdstone of Brisingamen',)
('Thud!',)











PS C:\Users\meast\Desktop\M04> & c:/Users/meast/Desktop/M04/env/Scripts/Activate.ps1
(env) PS C:\Users\meast\Desktop\M04>

(env) PS C:\Users\meast\Desktop\M04> import csv
import : The term 'import' is not recognized as the name of a cmdlet, function, script file, 
or operable program. Check the spelling of the name, or if a path was included, verify that 
the path is correct and try again.
At line:1 char:1
+ import csv
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (import:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(env) PS C:\Users\meast\Desktop\M04> python
Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import csv
>>> import sqlite3
>>> ins_str = 'insert into book values(?, ?, ?)'
>>> with open('books.csv', 'rt') as infile:
...     books = csv.DictReader(infile)
...     for book in books:
...             curs.execute(ins_str, (book['title'], book['author'], book['year']))
... <sqlite3.Cursor object at 0x1007b21f0>
  File "<stdin>", line 5
    <sqlite3.Cursor object at 0x1007b21f0>
    ^
SyntaxError: invalid syntax
>>> db.commit()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'db' is not defined
>>> import csv
>>> import sqlite3
>>> db = sqlite3.connect('books.db')
>>> conn = sqlalchemy.create_engine('sqlite:///books.db')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqlalchemy' is not defined
>>> pip install flask-sqlalchemy
  File "<stdin>", line 1
    pip install flask-sqlalchemy
        ^^^^^^^
SyntaxError: invalid syntax
>>> ^Z

(env) PS C:\Users\meast\Desktop\M04> pip install flask-sqlalchemy
Requirement already satisfied: flask-sqlalchemy in c:\users\meast\desktop\m04\env\lib\site-packages (3.0.5)
Requirement already satisfied: flask>=2.2.5 in c:\users\meast\desktop\m04\env\lib\site-packages (from flask-sqlalchemy) (2.3.2)
Requirement already satisfied: sqlalchemy>=1.4.18 in c:\users\meast\desktop\m04\env\lib\site-packages (from flask-sqlalchemy) (1.4.48)
Requirement already satisfied: Werkzeug>=2.3.3 in c:\users\meast\desktop\m04\env\lib\site-packages (from flask>=2.2.5->flask-sqlalchemy) (2.3.6)
Requirement already satisfied: Jinja2>=3.1.2 in c:\users\meast\desktop\m04\env\lib\site-packages (from flask>=2.2.5->flask-sqlalchemy) (3.1.2)
Requirement already satisfied: itsdangerous>=2.1.2 in c:\users\meast\desktop\m04\env\lib\site-packages (from flask>=2.2.5->flask-sqlalchemy) (2.1.2)
Requirement already satisfied: click>=8.1.3 in c:\users\meast\desktop\m04\env\lib\site-packages (from flask>=2.2.5->flask-sqlalchemy) (8.1.3)
Requirement already satisfied: blinker>=1.6.2 in c:\users\meast\desktop\m04\env\lib\site-packages (from flask>=2.2.5->flask-sqlalchemy) (1.6.2)
Requirement already satisfied: greenlet!=0.4.17 in c:\users\meast\desktop\m04\env\lib\site-packages (from sqlalchemy>=1.4.18->flask-sqlalchemy) (2.0.2)
Requirement already satisfied: colorama in c:\users\meast\desktop\m04\env\lib\site-packages (from click>=8.1.3->flask>=2.2.5->flask-sqlalchemy) (0.4.6)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\meast\desktop\m04\env\lib\site-packages (from Jinja2>=3.1.2->flask>=2.2.5->flask-sqlalchemy) (2.1.3)

[notice] A new release of pip available: 22.3.1 -> 23.1.2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlalchemy
>>> conn = sqlalchemy.create_engine('sqlite:///books.db')
>>> sql = 'select title from book order by title asc'
>>> rows = conn.execute(sql)
<stdin>:1: RemovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0. To prevent incompatible upgrades prior to updating applications, ensure requirements files are pinned to "sqlalchemy<2.0". Set environment variable SQLALCHEMY_WARN_20=1 to show all deprecation warnings.  Set environment variable SQLALCHEMY_SILENCE_UBER_WARNING=1 to silence this message. (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
>>>