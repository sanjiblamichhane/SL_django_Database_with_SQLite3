## Updata Records 
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance


## Update a Record
# we want to updata customers table
# let's see this method first
c.execute("""UPDATE customers SET first_name = 'Bob'
	WHERE last_name = 'Elder'
	""")

## commit the changes to db
conn.commit()
## what we will see is the first item is renamed as Bob Elder

## Query the database
c.execute("SELECT * FROM customers ")

## print items after the update
items = c.fetchall()

## print items
for item in items:
	print(item)

print('\nCommand executed successfully...')


## close our connection
conn.close()

