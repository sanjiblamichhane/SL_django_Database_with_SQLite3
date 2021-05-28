import sqlite3

## Query the database and return all records
def show_all():
	## CONNECT TO DATABASE
	conn = sqlite3.connect('customer.db')

	## CREATE A CURSOR
	c = conn.cursor()

	## Query database
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()

	## print all items
	for item in items:
		print(item)

	## commit the changes to db
	conn.commit()

	## close our connection
	conn.close()

## function that adds one record to the table
def add_one(first, last, email):
	## CONNECT TO DATABASE
	conn = sqlite3.connect('customer.db')

	## CREATE A CURSOR
	c = conn.cursor()

	## Query database
	c.execute("INSERT INTO customers VALUES (?,?,?)",(first, last, email)) 

	## commit the changes to db
	conn.commit()

	## close our connection
	conn.close()

## delete a Record from Table
def delete_one(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("DELETE from customers WHERE rowid = (?)", id)

	## commit our command and close
	conn.commit()
	conn.close()
