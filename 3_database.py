import sqlite3

conn = sqlite3.connect('customer.db') # store db in memory

# create a cursor
c = conn.cursor()#cursor() instance

## QUERY THE DATABASE
c.execute("SELECT * FROM customers")
c.fetchone()
#c.fetchmany(3)
#c.fetchall()
#print(c.fetchall())



print('Command executed successfully...')
## commit the changes to db
conn.commit()

## close our connection
conn.close()
