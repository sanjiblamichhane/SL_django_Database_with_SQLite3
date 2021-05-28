import database

## add_one() function
#database.add_one("Prithvi", "Narayan Shah", "gorkha@977.com")


## delete one
#database.delete_one('6')	## pass the id as string not plain integer



## add many records
#stuff = [
#	('SL','Lamic','sample@leehhane.com'),
#	('SL','Lamic','sample@leehhane.com'),
#	('robofriends','jax','jax@robo.com')
#]
#database.add_many(stuff)	## call the add_many() function



## LOOKUP EMAIL ADDRESS
database.email_lookup("jax@robo.com")

## show all the records
#database.show_all()	# call the function from database.py


