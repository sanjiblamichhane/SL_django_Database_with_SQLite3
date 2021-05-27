## Order Results by:
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## Query the database - Order by
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid ")

## sort in descending order of ids
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

## commit the changes to db
conn.commit()
## what we will see is the first item is renamed as Bob Elder

## print items after the update
items = c.fetchall()

## print items
for item in items:
	print(item)

print('\nCommand executed successfully...')


## close our connection
conn.close()

