## Update a Record 
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance


## Update a Record
# we want to updata customers table
# This will update the Bob of the first row only unlike the previous example where all Bobs with same last names were updated 
c.execute("""UPDATE customers SET first_name = 'John'
	WHERE rowid=1
	""")

c.execute("""UPDATE customers SET first_name = 'Marty'
	WHERE rowid=4 
	""")

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

