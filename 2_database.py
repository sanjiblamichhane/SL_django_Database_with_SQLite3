import sqlite3


#create connection
#conn = sqlite3.connect(':memory:') # store db in memory

##

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## insert a record into the table
#c.execute("INSERT INTO customers VALUES ('John','Elder','john123@domain.com')")

## insert many record into the table

many_customers = [('Wes','Brown','wes@browwn.com'),
		 ('Steph','Kuewa','steph@kuewa.com'),
		 ('Dan','Pas','dan@pas.com'),
		 ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers) # ? is place holder -->  
print('Command executed successfully...')
## commit the changes to db
conn.commit()

## close our connection
conn.close()
