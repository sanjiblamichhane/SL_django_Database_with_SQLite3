## Delete a Record 
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance
###########################################
## Delete a record
c.execute("DELETE from customers WHERE rowid = 6")

###########################################

## commit the changes to db
conn.commit()
## what we will see is the first item is renamed as Bob Elder

## Query the database
c.execute("SELECT rowid, * FROM customers ")

## print items after the update
items = c.fetchall()

## print items
for item in items:
	print(item)

print('\nCommand executed successfully...')


## close our connection
conn.close()

