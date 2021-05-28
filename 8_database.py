## Primary Keys 
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## QUERY THE DATABASE
c.execute("SELECT * FROM customers")


## print row-ids in front of the table
c.execute("SELECT rowid, * FROM customers")#select rowid and everything from customers


#print(c.fetchone())
#c.fetchmany(3)
#c.fetchall()
#print(c.fetchall())

items = c.fetchall()

## print items
for item in items:
	print(item)

print('\nCommand executed successfully...')
## commit the changes to db
conn.commit()

## close our connection
conn.close()
