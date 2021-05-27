import sqlite3


#create connection
#conn = sqlite3.connect(':memory:') # store db in memory

##

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## insert a record into the table
c.execute("INSERT INTO customers VALUES ('John','Elder','john123@domain.com')")
c.execute("INSERT INTO customers VALUES ('John2','Elder2','john2@domain.com')")
c.execute("INSERT INTO customers VALUES ('John3','Elder2','john3@domain.com')")
c.execute("INSERT INTO customers VALUES ('John3','Elder3','john3@domain.com')")

print('Command executed successfully...')
## commit the changes to db
conn.commit()

## close our connection
conn.close()
