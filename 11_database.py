## Primary Keys ..contd
# pulling out specific things from our database --> Email
# for example: searching for an item
#################################################################################
import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## QUERY THE DATABASE
c.execute("SELECT * FROM customers")


## QUERY THE DATABASE
## we could also do LIKE to search for like-items
c.execute("SELECT * FROM customers WHERE email LIKE '%@domain.com' ")#select rowid and everything from customers


items = c.fetchall()

## print items
for item in items:
	print(item)

print('\nCommand executed successfully...')
## commit the changes to db
conn.commit()

## close our connection
conn.close()
