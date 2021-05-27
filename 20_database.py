## LIMITING RESULTS
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## Query the database - Order by
## get items with multiple conditions
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")

## print items after the update
items = c.fetchall()

## print items
for item in items:
	print(item)

print('\nCommand executed successfully...')


## commit the changes to db
conn.commit()
## what we will see is the first item is renamed as Bob Elder

## close our connection
conn.close()

