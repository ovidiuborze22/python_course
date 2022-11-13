# interacting with PostgreSQL databases 

# importing psycopg2 library
import psycopg2

# connecting or creating to an SQLite databases with python
def create_table():
    conn=psycopg2.connect("dbname='db' user='postgres' password='admin' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

# inserting values into database
def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='db' user='postgres' password='admin' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()



# selecting all Records from database and displaying them
def view():
    conn=psycopg2.connect("dbname='db' user='postgres' password='admin' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

# deleting PostgreSQL Records from database
def delete(item):
    conn=psycopg2.connect("dbname='db' user='postgres' password='admin' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

# updating Records from database
def update(quantity,price,item):
    conn=psycopg2.connect("dbname='db' user='postgres' password='admin' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

#create_table()
#insert("Banana",4,2)
update(20,5.0,"Apple")
#delete("Banana")
print(view()) 
#insert("Coffee Cup",11,7)