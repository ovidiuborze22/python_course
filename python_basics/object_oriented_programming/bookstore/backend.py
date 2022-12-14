# coding the backend
import sqlite3

class Database:
    
    # function to connect database
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        

    # function to insert values into database
    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
       
    # function to view all records from database
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    # function to search records by title,author,year or isbn
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    # function to delete records from database
    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
       
    
    # function to update records from database
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()

#connect()
#insert("The Sun", "John Tablet",2005,913123178)
#delete(1)
#update(4,"The moon","John Smooth",2010,9231293222)
#print(view())
#print(search(author="John Smith"))