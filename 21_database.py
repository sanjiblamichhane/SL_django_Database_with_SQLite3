## Dropping a table entirely
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## Drop Table
c.execute("DROP TABLE customers")
conn.commit()

## Query the database again and notice the change
c.execute("SELECT rowid, * FROM customers")



## print items after the update
items = c.fetchall()

## print items
for item in items:
	print(item)

print('\nCommand executed successfully...')


## close our connection
conn.close()

