# coding the backend
import sqlite3

# function to connect database
def connect():
    conn=sqlite3.connect("python_course/python_apps/App5_Build_a_Book_Inventory_Desktop_GUI_Database/books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

# function to insert values into database
def insert(title,author,year,isbn):
    conn=sqlite3.connect("python_course/python_apps/App5_Build_a_Book_Inventory_Desktop_GUI_Database/books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

# function to view all records from database
def view():
    conn=sqlite3.connect("python_course/python_apps/App5_Build_a_Book_Inventory_Desktop_GUI_Database/books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

# function to search records by title,author,year or isbn
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("python_course/python_apps/App5_Build_a_Book_Inventory_Desktop_GUI_Database/books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

# function to delete records from database
def delete(id):
    conn=sqlite3.connect("python_course/python_apps/App5_Build_a_Book_Inventory_Desktop_GUI_Database/books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()
 
# function to update records from database
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("python_course/python_apps/App5_Build_a_Book_Inventory_Desktop_GUI_Database/books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()
#insert("The Sun", "John Tablet",2005,913123178)
#delete(1)
#update(4,"The moon","John Smooth",2010,9231293222)
print(view())
print(search(author="John Smith"))