## Primary Keys ..contd
# pulling out specific things from our database
# for example: searching for an item
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## QUERY THE DATABASE
c.execute("SELECT * FROM customers")


## QUERY THE DATABASE
c.execute("SELECT * FROM customers WHERE last_name = 'Elder' ")#select rowid and everything from customers
# we can also add other parameters to search for
#c.execute("SELECT * FROM customers WHERE age>= 15, last_name = 'Elder' ")#select rowid and everything from customers

items = c.fetchall()

## print items
for item in items:
	print(item)

print('\nCommand executed successfully...')
## commit the changes to db
conn.commit()

## close our connection
conn.close()
