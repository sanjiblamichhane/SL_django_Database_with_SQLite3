import sqlite3


#create connection
#conn = sqlite3.connect(':memory:') # store db in memory

##

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## insert a record into the table
#c.execute("INSERT INTO customers VALUES ('John','Elder','john123@domain.com')")
#create a table
c.execute("""CREATE TABLE customers(
	first_name text,
	last_name text,
	email text
	)""")

## data types in sqlite3
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

## commit the changes to db
conn.commit()

## close our connection
conn.close()
