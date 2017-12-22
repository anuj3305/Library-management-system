# -*- coding: utf-8 -*-
import io
	# ----- DUMP BOOKS.CSV TO LIBRARY.SQL ----- #
list = []
with io.open(r'C:\Users\anuj3\Desktop\Project\books.csv', encoding = "utf-8") as f:
    for line in f:
        temp = []
        for word in line.split('\t'):
            word = word.replace("'", "''")
            temp.append(word)
        list.append(temp)
f = io.open(r'library.sql', 'w', encoding = "utf-8")
f.write(unicode("drop schema if exists library;\n"))
f.write(unicode("create schema library;\n"))
f.write(unicode("use library;\n\n\n"))
f.write(unicode("create table book(isbn varchar(10),title varchar(500),primary key(isbn));\n"))
f.write(unicode("create table authors(author_id int,name varchar(50),primary key(author_id));\n"))
f.write(unicode("create table book_authors(author_id int,isbn varchar(10),primary key(author_id,isbn),foreign key(author_id) references authors(author_id),foreign key(isbn) references book(isbn));\n"))
f.write(unicode("create table borrower(Card_ID int,Ssn varchar(11),Bname varchar(50),Address varchar(100),Phone varchar(15),primary key(Card_ID), unique(Ssn));\n"))
f.write(unicode("create table book_loans(loan_id int,isbn varchar(10),card_id int,date_out date,due_date date,date_in date,primary key(loan_id),foreign key(isbn) references book(isbn),foreign key(card_id) references borrower(card_id));\n"))
f.write(unicode("create table fines(loan_id int,fine_amt decimal(10,2),paid bool,primary key(loan_id),foreign key(loan_id) references book_loans(loan_id));\n\n\n"))
book = []
authors = []
book_authors = []
for i in list[1:]:
    temp = []
    temp_book_authors = []
    temp.append(i[0])
    temp_book_authors.append(i[0])
    temp.append(i[2])
    temp_book_authors.append(i[2])
    ta = []
    for x in i[3].split(','):
        ta.append(x)
    temp_book_authors.append(ta)
    book.append(temp)
    authors.append(i[3])
    book_authors.append(temp_book_authors)
for i in book:
    f.write(unicode("insert into book values('"+i[0]+"','"+i[1]+"');\n"))

new_authors = []   
for i in authors:
    for x in i.split(','):
        new_authors.append(x)
new_authors = set(new_authors)

new_authors_1 = []
for i in new_authors:
    new_authors_1.append(i)
autid = []
for i in range(1,len(new_authors_1)):
    temp = []
    temp.append(i)
    temp.append(new_authors_1[i])
    autid.append(temp)
    f.write(unicode("insert into authors values("+str(i)+",'"+new_authors_1[i]+"');\n"))
bookaut = []
for i in book_authors:
    for j in i[2]:
        temp = []
        temp.append(i[0])
        for k in autid:
            if(k[1] == j):
                temp.append(k[0])
        if(len(temp) == 2):
            bookaut.append(temp)
bookauthor = []
for i in bookaut:
    flag = 0
    for j in bookauthor:
        if(i[0] == j[0] and j[1] == i[1]):
            flag = 1
            break;
    if(flag == 0):
        bookauthor.append(i)
for i in bookauthor:
    f.write(unicode("insert into book_authors values("+str(i[1])+",'"+str(i[0])+"');\n"))
	
	
	# ----- DUMP BORROWER.CSV TO LIBRARY.SQL ----- #
borrower = []
with open(r'C:\Users\anuj3\Desktop\Project\borrowers.csv') as f:
    for line in f:
        temp = []
        for word in line.split(','):
            word = word.replace("\n","")            
            temp.append(word)
        borrower.append(temp)
bw=[]
for i in borrower[1:]:
    temp = []
    temp.append(i[0])
    temp.append(i[1])
    temp.append(i[2] + " " + i[3])
    add = i[5] + "," + i[6] + "," + i[7]
    temp.append(add)
    temp.append(i[8])
    bw.append(temp)
f = io.open('library.sql', 'a', encoding="utf-8")
for i in bw:
    f.write(unicode("insert into borrower values("+i[0]+",'"+i[1]+"','"+i[2]+"','"+i[3]+"', '"+i[4]+"');\n"))
