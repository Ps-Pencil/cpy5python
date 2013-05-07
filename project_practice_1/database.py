import sqlite3

items="""A4 lecture pad
2.60
7-colour sticky note with pen
4.20
A5 ring book
4.80
A5 note book with zip bag
4.60
2B pencil
0.90
Stainless steel tumbler
12.90
A4 clear holder
4.40
A4 vanguard file
1.00
Name card holder
10.90
Umbrella
9.00
School badge (Junior High)
1.30
School badge (Senior High)
1.80
Dunman dolls (pair)
45.00
"""
item_list=items.split('\n')

with sqlite3.connect("model.db") as connection:
	c=connection.cursor()
	c.execute("drop table if exists users")
	c.execute("CREATE TABLE users (username TEXT, password TEXT, email TEXT)")
	c.execute("drop table if exists items")
	c.execute("CREATE TABLE items (name TEXT, price REAL, quantity INT)")
	for i in range(0,len(item_list)-1,2):
		c.execute("insert into items values(?,?,?)",[item_list[i],float(item_list[i+1]),10])
	c.execute("drop table if exists orders")
	c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, username TEXT, total REAL, pad INT,note INT, book INT, bag INT, pencil INT, tumbler INT, holder INT, file INT, cardholder INT, umbrella INT, jhbadge INT, shbadge INT, doll INT, time TEXT)")





