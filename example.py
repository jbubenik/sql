import sqlite3

con = sqlite3.connect("survey.db")
cur = con.cursor()
cur.execute("SELECT * FROM Person;")
results = cur.fetchall()

for i in results:
	print(i)
	
cur.close()
con.close()

