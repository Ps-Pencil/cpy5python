import sqlite3


d=[('a',1),('b',2),('c',3),('d',4),('e',5),('f',6),('g',7),('h',8),('i',9),('j',10)]

with sqlite3.connect('sales.db') as connection:
	c=connection.cursor()
	c.execute("DROP TABLE if exists reps")
	c.execute('''CREATE TABLE reps (rep_name TEXT,amount INT)''')
	c.executemany("INSERT INTO reps VALUES(?,?)", d)