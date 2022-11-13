# interacting with databases

# importing sqlite3 library
import sqlite3

# connecting or creating to an SQLite databases with python
def create_table():
    conn=sqlite3.connect("python_course/python_basics/interaction_with_databases/lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

# inserting values into database
def insert(item,quantity,price):
    conn=sqlite3.connect("python_course/python_basics/interaction_with_databases/lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()



# selecting all Records from database and displaying them
def view():
    conn=sqlite3.connect("python_course/python_basics/interaction_with_databases/lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

# deleting SQl Records from database
def delete(item):
    conn=sqlite3.connect("python_course/python_basics/interaction_with_databases/lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

# updating Records from database
def update(quantity,price,item):
    conn=sqlite3.connect("python_course/python_basics/interaction_with_databases/lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

update(11,6,"Water Glass")
#delete("Coffee Cup")
print(view()) 
#insert("Coffee Cup",11,7)